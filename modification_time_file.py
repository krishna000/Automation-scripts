# Q1: Find the modification time of a file

import os
import time

file_path = "access.log"
mod_time = os.path.getmtime(file_path)

print("Modification time (raw): ", mod_time)
print("Readable time: ",time.ctime(mod_time))