#!/usr/bin/python3
import os
import sys
import json

print("Mounting Drive...")
os.system("mkdir -p /home/gdrive && rclone mount drive: /home/gdrive  --umask 0000  --default-permissions  --allow-non-empty  --allow-other  --buffer-size 32M  --dir-cache-time 12h  --vfs-read-chunk-size 64M  --vfs-read-chunk-size-limit 1G & ")
print("Reading config..")
fobj = open("config.json")
fp = json.load(fobj)

print("Writing Script...")
with open("script.sh", 'w') as f:
    f.write("#!/bin/sh\n")
    for k,v  in fp.items():
        f.write('wget -O "' + str(k) + '" --no-check-certificate "' + str(v) + '"\n')

print("Process exited.")
