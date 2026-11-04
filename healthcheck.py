"""healthcheck - check how full the disk is."""
import json
import shutil
import sys


def disk_usage_percent(path="/"):
    """Return how full the disk is, as a whole number (0-100)."""
    usage = shutil.disk_usage(path)
    return round(usage.used / usage.total * 100)

def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    paths = [arg for arg in args if arg != "--json"]
    path = paths[0] if paths else "/"

    percent = disk_usage_percent(path)
    status = get_status(percent)

    if as_json:
        print(json.dumps({"path": path, "percent": percent, "status": status}))
    else:
        print(f"[{status}] Disk usage on {path}: {percent}%")
    
def get_status(percent):
    if percent >= 90:
        return "CRIT"
    if percent >= 80:
        return "WARN"
    return "OK"

if __name__ == "__main__":
    main()
