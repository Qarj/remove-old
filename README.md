# remove-old 0.1.0
Removes old files.

## Use Cases:
* cleaning up old log files
* cleaning up old automated regression test results

## Features:
* will remove files recursively from given path older than a given number of days
* empty folders will be removed regardless of their age
* hidden and read-only files are removed
* statistics showing number of files and folders deleted shown
* verbose mode lists every file and folder removed
* much faster than shift-delete from Windows Explorer - approx 5x faster!