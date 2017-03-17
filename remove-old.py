#!/usr/bin/env python3

version="0.1.0"

import os, time, argparse, stat

def flushdir(dir, days_old, verbose):
    files_removed = 0
    folders_removed = 0
    if not os.path.isdir(dir):
        print ("Folder", dir, "not found")
        return 0, 0
    now = time.time()
    for file_name in os.listdir(dir):
        file_full = os.path.join(dir, file_name)
        if os.path.isdir(file_full):
            sub_files_removed, sub_folders_removed = flushdir(file_full, days_old, verbose)
            files_removed += sub_files_removed
            folders_removed += sub_folders_removed
        elif os.stat(file_full).st_mtime < (now - 86400 * days_old): #86400 = 1 day
            if os.path.isfile(file_full):
                try:
                    os.remove(file_full)
                    if verbose:
                        print ("Removed:", file_full)
                    files_removed += 1
                except PermissionError:
                    os.chmod(file_full, stat.S_IWRITE) # remove read-only flag
                    os.remove(file_full)
                    if verbose:
                        print ("Forcibly removed:",file_full)
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

print ("Remove files older than", args.days_old, "days from", args.path)

files_removed, folders_removed = flushdir(args.path, args.days_old, args.verbose)
print ("Removed",files_removed,"files and",folders_removed,"folders")
