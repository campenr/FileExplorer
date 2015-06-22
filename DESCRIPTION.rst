This module is built for python 3, and is not backwards compatible
with python 2. 

This module includes a number of functions that provide basic 
directory browser functionality, in an easy to view format, within a 
command line environment, e.g. cmd.exe. Using the main function
browse_dir() allows the user to browse the directory tree and set the
current working directory. Another function, select_files() can be 
used to return a list of files within that directory, optionally 
filtered by file type. 

The display of the directory is formatted as follows, where the 
ellipsis, '...', represents the parent directory: ::

[0] ...
[1] Folder1
[2] File1.py
[3] File2.txt
[4] Folder2