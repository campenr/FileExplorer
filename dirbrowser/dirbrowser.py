# Copyright 2015 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Module that enables basic file/directory browser functionality.

dirbrowser version 1.0a2
========================

This module includes a number of functions that provide basic directory
browser functionality in an easy to view format within a command 
line environment, e.g. Windows shell. Using the two main functions
browse_dir() and select_files() in combination allows the user
to browse the directory tree and set a working directory, and return
a list of files within that directory, optionally filtered by file
type. This list of files can then be utilised by other scripts.

TODO:
- add support for selecting multiple files in select_files() instead
  of either all or one

See README.txt for full documentation.
"""

import os

def list_children(directory, filter_type=None, file_filter=None,
                  show_parent=True):
    """Create a list of the children in 'directory'.

    Children in a directory are stored in a list, which can be filtered
    to contain only files or directories by setting filter_type. Valid
    arguments are:

    None    - Does not filter children. Default option.
    'file'  - Filter only allows files
    'dir'   - Filter only allows directories

    If filter_type is set to "file", the child_list can be additionally
    filtered by the files extension by setting file_filter, which takes
    a string and matches it to the file name. If no files have a matching
    extension the resulting child_list will be empty.
    """

    child_list = list()
    list_dir = os.listdir(directory)

    # Get the list of children in the current directory, filtered
    # according to filter_type
    if filter_type == "dir":
        child_list = [child for child in list_dir
                      if os.path.isdir(child)]
    elif filter_type is None or filter_type == "file":
        if filter_type is None:
            child_list = list_dir
            # If filter_type is none then file_filter is set to None
            file_filter = None
        elif filter_type == "file":
            child_list = [child for child in list_dir
                          if os.path.isfile(child)]

    # If an incorrect filter_type is entered the default 'None' is
    # selected and a message printed to notify user
    else:
        print("Invalid filter selected, default of 'None' chosen")
        child_list = list_dir

    # Filter files by file_filter if filter_type = "file"
    if filter_type == "file":
        if file_filter is not None:
            child_list = [child for child in child_list
                          if child.endswith(file_filter)]

    # Prepend child_list with ".." placeholder for parent directory
    # if show_parent=True
    if show_parent is True:
        child_list.insert(0, "..")

    # Prepend child_list with an empty placeholder at 0th index
    child_list.insert(0, "")

    return child_list

def display_children(child_list):
    """Print child_list in an easy to read format.

    Takes the child_list object and displays it in an easy to read
    manner, with their indices for easy selection as shows:

    [1] ...
    [2] Folder1
    [3] File1.py
    [4] File2.txt
    [5] Folder2

    The 0th index is hidden and is a placeholder for selecting the
    current working directory.
    """

    for child in child_list[1::]:
        print("[{}] {}".format(child_list.index(child), child))

    return

def change_dir():
    """Change the current working directory to a child/parent directory.
 
    This function is intended to operate within a loop provided by
    another function, browse_dir().

    Displays the current working dictionary, and then displays the
    children in the current working directory (files and directories).
    User is prompted to select a new directory by entering the associated
    number. The function returns user input as dir_number.

    The user can select the current directory as the new working directory
    by selecting 0, causing the function to return False, and terminating
    the loop within which change_dir() is called in browse_dir().
    """

    # Obtains and prints the current working directory, and prints the
    # children by calling the list_children() function
    current_dir = os.getcwd()
    print(current_dir)
    child_list = list_children(current_dir)
    display_children(child_list)

    # Collect input from user and change the directory using the input to
    # index the child_list
    dir_number = int(input("Enter a number to select the corresponding "
                           "directory, or 0 to confirm current "
                           "directory: "))
    if dir_number == 0:
        return dir_number
    else:
        if child_list[dir_number] == "..":
            os.chdir(os.path.dirname(current_dir))
        else:
            sub_dir = child_list[dir_number]
            os.chdir(os.path.join(current_dir, sub_dir))

    return dir_number

def browse_dir():
    """Loop change_dir() to browse directory tree, and catch exceptions.

    Loops change_dir(), checking the output each time that dir_number is
    True. If False the loop is terminated and the current directory set
    as the working directory. This function also catches any exceptions
    encountered by change_dir() while attempting to change the directory.
    """

    # Generate loop to repeatedly request user to change directory while
    # checking the output of change_dir() and continuing loop while True
    while True:
        try:
            dir_number = change_dir()
            if not dir_number:
                print("\nSelected working directory is {}\n"
                      .format(os.getcwd()))
                return
        except NotADirectoryError:
            print("\nThat is not a valid directory\n")
        except ValueError:
            print("\nNot a valid selection\n")
        except KeyError:
            print("\nNot a valid selection\n")
        except PermissionError:
            print("\nInsufficient permissions. Try running as "
                  "administrator\n")
    return


def select_files(file_filter=None):
    """Generate a list of files as specified by user input.

    Files are selected by their number associated in the child_list
    object.

    To implement:
    - Enable selecting a subset of files instead of simply all or one
    """

    # Generate and display a list of the files in the current working
    # directory, filtered by file type if an argument is given
    directory = os.getcwd()
    child_list = list_children(directory, filter_type="file",
                               file_filter=file_filter, show_parent=False)
    display_children(child_list)

    file_select = input("Select a file using the associated number, or"
                        " 'all' to select all files: ")

    # Splice file_list according to user input and return a new list
    # The first, placeholder item in child_list is removed if 'all' selected
    if file_select == "all":
        file_list = child_list[1::]
    else:
        file_list = [child_list[int(file_select)]]

    return file_list


# Run browse_dir() to test code
browse_dir()
select_files()
