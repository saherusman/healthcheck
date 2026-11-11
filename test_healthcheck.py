import subprocess
import sys
from pathlib import Path

from healthcheck import get_status


def test_ok():
    assert get_status(50) == "OK"


def test_warn():
    assert get_status(85) == "WARN"


def test_crit():
    assert get_status(95) == "CRIT"


def test_limits():
    assert get_status(79) == "OK"
    assert get_status(80) == "WARN"
    assert get_status(90) == "CRIT"


def test_missing_path(tmp_path):
    missing_path = tmp_path / "missing.log"
    script = Path(__file__).with_name("healthcheck.py")

    result = subprocess.run(
        [sys.executable, str(script), str(missing_path)],
        capture_output=True,
        text=True,
	check=False,
    )

    assert result.returncode == 1
    assert f"Error: path '{missing_path}' does not exist." in result.stderr
    assert result.stdout == ""
