#Q3 Delete all the *.log files in a directory if it's older than 7 days.

import os

from file_older_than import seven_days, now
deleted = 0
not_deleted = 0
dir_path = "/var/log"
for file in os.listdir(dir_path):
    full_path = os.path.join(dir_path, file)

    if os.path.isfile(full_path) and file.endswith(".log"):
        mod_time = os.path.getmtime(full_path)
        if now - mod_time > seven_days:
            try:
                os.remove(full_path)
                deleted += 1
            except Exception as e:
                print(f"Failed to delete {file}: {e}")
                not_deleted += 1
print(f"deleted: {deleted}")
print(f"not_deleted: {not_deleted}")

