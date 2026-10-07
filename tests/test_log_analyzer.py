from datetime import datetime
from pathlib import Path

from capstone.log_analyzer import (
    analyze_file,
    find_suspicious_ips,
    main,
    parse_line,
    parse_lines,
)

SAMPLE = Path(__file__).resolve().parent.parent / "sample_data" / "auth.log"


def test_parse_valid_line():
    e = parse_line("2026-10-01 08:02:11 FAILED user=admin ip=203.0.113.7")
    assert e.status == "FAILED" and e.user == "admin" and e.ip == "203.0.113.7"
    assert e.timestamp == datetime(2026, 10, 1, 8, 2, 11)


def test_parse_rejects_malformed_lines():
    assert parse_line("garbage") is None
    assert parse_line("2026-13-01 08:02:11 FAILED user=a ip=1.2.3.4") is None
    assert parse_line("2026-10-01 08:02:11 MAYBE user=a ip=1.2.3.4") is None
    assert parse_line("2026-10-01 08:02:11 FAILED name=a ip=1.2.3.4") is None


def test_parse_lines_skips_comments_and_counts_bad_lines():
    events, skipped = parse_lines(["# comment", "", "bad line",
                                   "2026-10-01 08:00:00 SUCCESS user=a ip=192.0.2.1"])
    assert len(events) == 1 and skipped == 1


def test_sliding_window():
    lines = [f"2026-10-01 08:00:{s:02d} FAILED user=root ip=203.0.113.9" for s in (0, 10, 20)]
    lines += [f"2026-10-01 0{h}:00:00 FAILED user=guest ip=198.51.100.1" for h in (1, 2, 3)]
    events, _ = parse_lines(lines)
    flagged = find_suspicious_ips(events, threshold=3, window_seconds=60)
    assert flagged == {"203.0.113.9": 3}  # slow, spread-out failures are not flagged


def test_analyze_sample_file():
    report = analyze_file(SAMPLE, threshold=3, window_seconds=300)
    assert report["skipped"] == 1
    assert report["failed_by_ip"]["203.0.113.7"] == 5
    assert report["failed_by_ip"]["198.51.100.23"] == 3
    assert report["suspicious"] == {"203.0.113.7": 5}


def test_cli(capsys):
    assert main([str(SAMPLE)]) == 0
    out = capsys.readouterr().out
    assert "ALERT" in out and "203.0.113.7" in out
    assert main(["does-not-exist.log"]) == 1
