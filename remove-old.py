#!/usr/bin/env python3

version="0.0.4"

# http://stackoverflow.com/questions/7217196/python-delete-old-files
import os, time, argparse, stat

path = "\\inetpub\\wwwroot\\TLD"
def flushdir(dir, days_old, verbose):
    files_removed = 0
    folders_removed = 0
    if not os.path.isdir(dir):
        print ("Folder", dir, "not found")
        return 0, 0
    now = time.time()
    for f in os.listdir(dir):
        fullpath = os.path.join(dir, f)
        if os.path.isdir(fullpath):
            files_removed, folders_removed = flushdir(fullpath, days_old, verbose)
        elif os.stat(fullpath).st_mtime < (now - 86400 * days_old): #86400 = 1 day
            if os.path.isfile(fullpath):
                try:
                    os.remove(fullpath)
                    if verbose:
                        print ("Removed:",fullpath)
                    files_removed += 1
                except PermissionError:
                    os.chmod( fullpath, stat.S_IWRITE ) # remove read-only flag
                    os.remove(fullpath)
                    if verbose:
                        print ("Forcibly removed:",fullpath)
                    files_removed += 1
    if not os.listdir(dir):
        if verbose:
            print ("Removed empty folder:",dir)
        os.rmdir(dir)
        folders_removed += 1
    return files_removed, folders_removed

parser = argparse.ArgumentParser(description='Remove old files from specified path.')
parser.add_argument('path', metavar='PATH', help='folder path to recursively remove old files')
parser.add_argument('--older-than-days', dest='days_old', required=True, type=int, action='store', help='Files older than integer days will be removed')
parser.add_argument('--version', action='version', version=version)
parser.add_argument('--verbose', action='store_true', dest='verbose', default=False, help='Will output names of files and folders deleted')
args = parser.parse_args()

print ("Remove files older than", args.days_old, "days")
print ("From", args.path)
print ("Verbose:", args.verbose)

files_removed, folders_removed = flushdir(args.path, args.days_old, args.verbose)
print ("Removed",files_removed,"files and",folders_removed,"folders")

# To Do:
#   x pass parameter from command line - number of days old
#   x do not look at the folder age, recursively search all sub folders
#   x after completing one folder, check if the folder is empty, if so, remove the folder
#   x ensure that hidden files are removed
#   x ensure that read only files are removed
#   x ensure that spaces in file names / folder names are handled
#   x non-existant path is handled gracefully
#   x --verbose - every file and folder name removed is shown
#   x add version info
#   - tidy up outputl