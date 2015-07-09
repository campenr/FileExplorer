dirbrowser version 1.0a2
========================


Bugs and issue tracking
-----------------------

This module should be platform independent, however testing has to
date only been performed with Windows 8.1 Pro using cmd.exe. Bug
reports should be submitted via the github issue tracker.


Usage
-----

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

Using browse_dir() the children within a directory can be viewed,
the directory tree traversed, and the working directory set. The
browse_dir() function is a wrapper for the change_dir() function
that creates and displays the children of the current directory.
This is done with with calls to create_child_dict(), which takes a
list of children and adds to a dictionary object, and 
display_children() which displays the contents of the dictionary in
the above format.

The select_files() function displays the file child objects of the
current working directory, and allows the user to specify whether to
select all files or a single file, returning a list of the selected 
file(s). The files viewed using select_files() can be filtered for a
specific file type by preprocessing the file_list object passed to 
select_files() with the function filter_file_type(), and specifying 
the file suffix of the files to be returned. Optionally, 
user_input_file_type(), a wrapper for filter_file_type, prompts the
user to enter a file type suffix at the command line.

TODO
----

- Update documentation to give better usage examples
- Add support for selecting subsets of files instead of only all or 1
- Alter reporting of current directory if path is more than n items to
  display the current path in a more friendly way


License
-------

This software is released under the Modified BSD license. See 
LICENSE.txt for the full license.