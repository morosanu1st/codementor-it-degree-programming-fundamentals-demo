"""Capstone part 2 - Log-file analyzer that flags repeated failed logins.

Uses lessons 03-08: loops, functions, dicts, files, error handling, classes.
This is the same idea a real SIEM / fail2ban rule uses to spot brute-force
attacks, just much smaller.

Log format (one event per line):
    2026-10-01 08:15:02 FAILED user=admin ip=203.0.113.7
    2026-10-01 08:16:40 SUCCESS user=student ip=192.0.2.10

Run:  python -m capstone.log_analyzer sample_data/auth.log --threshold 3 --window 300
"""
import argparse
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass
class LoginEvent:
    timestamp: datetime
    status: str      # "FAILED" or "SUCCESS"
    user: str
    ip: str


def parse_line(line):
    """Turn one log line into a LoginEvent, or None if the line is malformed."""
    parts = line.split()
    if len(parts) != 5:
        return None
    date_part, time_part, status, user_field, ip_field = parts
    if status not in ("FAILED", "SUCCESS"):
        return None
    if not user_field.startswith("user=") or not ip_field.startswith("ip="):
        return None
    try:
        timestamp = datetime.strptime(f"{date_part} {time_part}", TIME_FORMAT)
    except ValueError:
        return None
    return LoginEvent(timestamp, status, user_field[5:], ip_field[3:])


def parse_lines(lines):
    """Parse many lines; return (events, number_of_skipped_lines)."""
    events, skipped = [], 0
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        event = parse_line(line)
        if event is None:
            skipped += 1
        else:
            events.append(event)
    return events, skipped


def failed_counts_by_ip(events):
    counts = {}
    for e in events:
        if e.status == "FAILED":
            counts[e.ip] = counts.get(e.ip, 0) + 1
    return counts


def find_suspicious_ips(events, threshold=3, window_seconds=300):
    """Return {ip: max failures seen inside any sliding window} for IPs that
    reached `threshold` failures within `window_seconds`."""
    failures = {}
    for e in sorted(events, key=lambda ev: ev.timestamp):
        if e.status == "FAILED":
            failures.setdefault(e.ip, []).append(e.timestamp)

    window = timedelta(seconds=window_seconds)
    suspicious = {}
    for ip, times in failures.items():
        start = 0
        best = 0
        for end in range(len(times)):
            while times[end] - times[start] > window:
                start += 1
            best = max(best, end - start + 1)
        if best >= threshold:
            suspicious[ip] = best
    return suspicious


def analyze_file(path, threshold=3, window_seconds=300):
    with open(path, encoding="utf-8") as f:
        events, skipped = parse_lines(f)
    return {
        "events": len(events),
        "skipped": skipped,
        "failed_by_ip": failed_counts_by_ip(events),
        "suspicious": find_suspicious_ips(events, threshold, window_seconds),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Flag IPs with repeated failed logins.")
    parser.add_argument("logfile")
    parser.add_argument("--threshold", type=int, default=3,
                        help="failures needed to flag an IP (default 3)")
    parser.add_argument("--window", type=int, default=300,
                        help="sliding window in seconds (default 300)")
    args = parser.parse_args(argv)

    try:
        report = analyze_file(args.logfile, args.threshold, args.window)
    except FileNotFoundError:
        print(f"error: file not found: {args.logfile}", file=sys.stderr)
        return 1

    print(f"Parsed {report['events']} events ({report['skipped']} malformed lines skipped)")
    print("Failed logins per IP:")
    for ip, count in sorted(report["failed_by_ip"].items(), key=lambda kv: -kv[1]):
        print(f"  {ip:<15} {count}")
    if report["suspicious"]:
        print(f"ALERT - {args.threshold}+ failures within {args.window}s:")
        for ip, count in sorted(report["suspicious"].items()):
            print(f"  {ip:<15} {count} failures")
    else:
        print("No suspicious activity found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
