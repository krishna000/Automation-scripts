import os
import time

file_path = "access.log"
mod_time = os.path.getmtime(file_path)

now = time.time()
seven_days = 7 * 24 * 60 * 60

if now - mod_time > seven_days:
    print(f"{file_path} is older than 7 days")
else:
    print(f"{file_path} is recent")