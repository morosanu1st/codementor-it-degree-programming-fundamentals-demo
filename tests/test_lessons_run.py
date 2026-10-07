"""Every lesson script must run from start to finish without errors."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LESSONS = sorted((ROOT / "lessons").glob("[0-9][0-9]_*.py"))


def test_there_are_eight_lessons():
    assert len(LESSONS) == 8


@pytest.mark.parametrize("script", LESSONS, ids=lambda p: p.name)
def test_lesson_runs(script):
    result = subprocess.run([sys.executable, str(script)], capture_output=True,
                            text=True, timeout=30, cwd=ROOT)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()


@pytest.mark.parametrize("module", ["capstone.hashing_demo"])
def test_capstone_demo_runs(module):
    result = subprocess.run([sys.executable, "-m", module], capture_output=True,
                            text=True, timeout=60, cwd=ROOT)
    assert result.returncode == 0, result.stderr
