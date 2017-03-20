# remove-old 0.2.0
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
* locked files and folders are skipped with a count of exceptions shown at the end
* much faster than shift-delete from Windows Explorer - approx 5x faster!

## Examples:

### minimum options
```
C:\git\remove-old>remove-old.py C:\inetpub\wwwroot\DEV\2017\01\18 --older-than-days 10
```

stdout
```
Remove files older than 10 days from C:\inetpub\wwwroot\DEV\2017\01\18
Removed 1080 files and 27 folders, encountered 0 exceptions
```

### verbose
```
C:\git\remove-old>remove-old.py C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches --older-than-days 5 --verbose
```

stdout
```
Remove files older than 5 days from C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite\courses_CoursesHome-GUI_1001.txt
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite\courses_CoursesHome-GUI_1002.txt
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite\courses_CoursesHome-GUI_1003.txt
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite\courses_CoursesHome-GUI_1004.txt
Removed empty folder: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\CoursesWebsite.xml
Removed: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches\Summary.xml
Removed empty folder: C:\inetpub\wwwroot\DEV\2017\01\31\All_Batches
Removed 6 files and 2 folders
```

### path with spaces

```
C:\git\remove-old>remove-old.py "D:\temp\My Folder" --older-than-days 150
```

Single quotes do not work (on Windows, not sure about Linux).

### locked files and paths

```
remove-old.py C:\webinject\temp --older-than-days 2 --verbose
```

```
Remove files older than 2 days from C:\webinject\temp
Could not remove file C:\webinject\temp\enzo_CPQ-TotalJobs_59907\chromedriver.exe
Could not remove folder C:\webinject\temp\New folder
Removed 0 files and 0 folders, encountered 2 exceptions
```