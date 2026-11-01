"""healthcheck - check how full the disk is."""

import shutil


def disk_usage_percent(path="/"):
    """Return how full the disk is, as a whole number (0-100)."""
    usage = shutil.disk_usage(path)
    return round(usage.used / usage.total * 100)


def main():
    percent = disk_usage_percent("/")
    print(f"Disk usage on /: {percent}% - {get_status(percent)}")

def get_status(percent):
    if percent >= 90:
        return "CRIT"
    if percent >= 80:
        return "WARN"
    return "OK"

if __name__ == "__main__":
    main()
