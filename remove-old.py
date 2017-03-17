#!/usr/bin/env python3

# Version 0.0.1

# http://stackoverflow.com/questions/7217196/python-delete-old-files
import os, time

path = "\\inetpub\\wwwroot\\TLD"
def flushdir(dir):
    if not os.path.isdir(dir):
        print ("Folder", dir, "not found")
        return
    now = time.time()
    for f in os.listdir(dir):
        fullpath = os.path.join(dir, f)
        if os.path.isdir(fullpath):
            flushdir(fullpath)
        if os.stat(fullpath).st_mtime < (now - 1): #86400 = 1 day
            if os.path.isfile(fullpath):
                os.remove(fullpath)
                print ("Removed:",fullpath)
    if not os.listdir(dir):
        print ("Removed empty Folder:",dir)
        os.rmdir(dir)

flushdir(path)


# To Do:
#   - pass parameter from command line - number of days old
#   x do not look at the folder age, recursively search all sub folders
#   x after completing one folder, check if the folder is empty, if so, remove the folder
#   - ensure that hidden files are removed
#   x ensure that spaces in file names / folder names are handled
#   x non-existant path is handled gracefully