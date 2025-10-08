#Q count files be extention in a directory
import os
from collections import Counter

dir_path = "/var/log"
ext_counter = Counter()
for root, dirs, files in os.walk(dir_path):
    for file in files:
        _, ext = os.path.splitext(file)
        if ext:
            ext_counter[ext] += 1

for ext, count in ext_counter.most_common():
    print(f"{ext} -> {count} files")
