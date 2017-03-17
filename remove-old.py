#!/usr/bin/env python3

version="0.0.3"

# http://stackoverflow.com/questions/7217196/python-delete-old-files
import os, time, argparse, stat

path = "\\inetpub\\wwwroot\\TLD"
def flushdir(dir, days_old):
    if not os.path.isdir(dir):
        print ("Folder", dir, "not found")
        return
    now = time.time()
    for f in os.listdir(dir):
        fullpath = os.path.join(dir, f)
        if os.path.isdir(fullpath):
            flushdir(fullpath, days_old)
        elif os.stat(fullpath).st_mtime < (now - 86400 * days_old): #86400 = 1 day
            if os.path.isfile(fullpath):
                try:
                    os.remove(fullpath)
                    print ("Removed:",fullpath)
                except PermissionError:
                    os.chmod( fullpath, stat.S_IWRITE ) # remove read-only flag
                    os.remove(fullpath)
                    print ("Forcibly removed:",fullpath)
    if not os.listdir(dir):
        print ("Removed empty folder:",dir)
        os.rmdir(dir)

parser = argparse.ArgumentParser(description='Remove old files from specified path.')
parser.add_argument('path', metavar='PATH', help='folder path to recursively remove old files')
parser.add_argument('--older-than-days', dest='days_old', required=True, type=int, action='store', help='files older than integer days will be removed')
args = parser.parse_args()
print ("Remove files older than", args.days_old, "days")
print ("From",args.path)

flushdir(args.path, args.days_old)
print ("All done")

# To Do:
#   x pass parameter from command line - number of days old
#   x do not look at the folder age, recursively search all sub folders
#   x after completing one folder, check if the folder is empty, if so, remove the folder
#   x ensure that hidden files are removed
#   x ensure that read only files are removed
#   x ensure that spaces in file names / folder names are handled
#   x non-existant path is handled gracefully
#   - stats-only parm - sum of folders and files deleted output instead of every file removed
#   - add version info