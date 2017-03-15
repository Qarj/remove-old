#!/usr/bin/env python3

# Version 0.0.1

# http://stackoverflow.com/questions/7217196/python-delete-old-files
import os, time

path = "/path/to/folder"
def flushdir(dir):
    now = time.time()
    for f in os.listdir(dir):
        fullpath = os.path.join(dir, f)
        if os.stat(fullpath).st_mtime < (now - 86400):
            if os.path.isfile(fullpath):
                os.remove(fullpath)
            elif os.path.isdir(fullpath):
                flushdir(fullpath)

flushdir(path)


# To Do:
#   - pass parameter from command line - number of days old
#   - do not look at the folder age, recursively search all sub folders
#   - after completing one folder, check if the folder is empty, if so, remove the folder
#   - ensure that hidden files are removed
#   - ensure that spaces in file names / folder names are handled