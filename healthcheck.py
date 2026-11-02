"""healthcheck - check how full the disk is."""

import shutil
import sys


def disk_usage_percent(path="/"):
    """Return how full the disk is, as a whole number (0-100)."""
    usage = shutil.disk_usage(path)
    return round(usage.used / usage.total * 100)



def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/"
    percent = disk_usage_percent(path)
    print(f"[{get_status(percent)}] Disk usage on {path}: {percent}%")
    

def get_status(percent):
    if percent >= 90:
        return "CRIT"
    if percent >= 80:
        return "WARN"
    return "OK"

if __name__ == "__main__":
    main()
