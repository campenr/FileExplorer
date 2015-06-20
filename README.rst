dirbrowser version 1.0a1
========================


Bugs and issue tracking
-----------------------

This module should be platform independent, however testing has to
date only been performed with Windows 8.1 Pro using cmd.exe. Bug
reports should be submitted via the github issue tracker.


Documentation
-------------

This software is built for python 3, and is not backwards compatible
with python 2. 

This module includes a number of functions that provide basic file
explorer functionality in an easy to view format within a command 
line environment, e.g. Windows shell. Using the two main functions
browse_dir() and select_files() in combination allows the user
to browse the directory tree and set a working directory, and return
a list of files within that directory, optionally filtered by file
type. This list of files can then be utilised by other programs.

The display of the directory is formatted as follows, where the 
ellipsis, '...', represents the parent directory:

''
[0] ...
[1] Folder1
[2] File1.py
[3] File2.txt
[4] Folder2
''


Using browse_dir() the children within a directory can be viewed,
the directory tree traversed, and the working directory set. The
browse_dir() function is a wrapper for the change_dir() function
that creates and displays the children of the current directory
with calls to create_child_dict() and display_children() respectively.

The select_files() function displays the file child objects of the
current working directory, and allows the user to specify whether to
select all files or a single file, returning a list of the selected 
file(s). The files viewed using selct_files() can be filtered for a 
specific file type by preprocessing the file_list object passed to 
select_files() with the function filter_file_type(), and specifying 
the file suffix of the files to be returned. Optionally, 
user_input_file_type(), a wrapper for filter_file_type, prompts the
user to enter a file type suffix at the command line.


License
-------

This software is released under the Modified BSD license. See 
LICENSE.txt for the full license.