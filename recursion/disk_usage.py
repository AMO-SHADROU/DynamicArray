import os


def disk_usage(path):
    """Return the number of bytes used by a file/directory."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    return total
