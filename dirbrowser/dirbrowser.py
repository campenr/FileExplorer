# Copyright 2015 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Module that enables basic file/directory browser functionality.

dirbrowser version 1.0b1
========================

This module includes a number of functions that provide basic directory
browser functionality in an easy to view format, within a command
line environment, e.g. the Windows command shell.

For complete documentation see README.rst.
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
    a string and matches it to the file name. The file_filter argument
    must be a string which matches the file extension, with or without
    the period i.e. both '.txt', and 'txt' are valid arguments.

    NOTE: If no files have a matching extension the resulting child_list
    will be empty.
    """

    list_dir = os.listdir(directory)

    # Filter children to files or directories
    # TODO refactor these conditionals to be more concise
    if filter_type == "dir":
        child_list = [child for child in list_dir
                      if os.path.isdir(child)]
    elif filter_type is None:
        child_list = list_dir
    elif filter_type == "file":
        child_list = [child for child in list_dir
                      if os.path.isfile(child)]
    else:
        print("Invalid filter selected, default of 'None' chosen")
        child_list = list_dir

    # Filter files by file type
    if filter_type == "file" and file_filter is not None:
        child_list = [child for child in child_list
                      if child.endswith(file_filter)]

    # Use a '..' placeholder for parent directory when listing
    # directories.
    if show_parent is True:
        child_list.insert(0, "..")

    # Use an empty placeholder at 0th index so child indices
    # start at 1.
    # TODO use '.' and display?
    child_list.insert(0, "")

    return child_list

def display_children(child_list):
    """Print child_list in an easy to read format.

    Displays children and their indices for easy selection as shown:

    [1] ..
    [2] Folder1
    [3] File1.py
    [4] File2.txt
    [5] Folder2

    The 0th index is hidden and is a placeholder for selecting the
    current working directory.
    """

    # TODO Does this deserve it's own function? Place this into create_child_list?

    for idx, child in enumerate(child_list):
        if idx != 0:
            print("[{index}] {child_item}".format(index=idx, child_item=child))

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
    by selecting 0.
    """

    # Obtains and prints the current working directory, and prints the
    # children by calling the list_children
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
    """Loop change_dir to browse directory tree, and catch exceptions.

    Loops change_dir, checking the output each time that dir_number is
    True. If False the loop is terminated and the current directory set
    as the working directory.
    """

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

    See list_children for valid file_filter arguments.

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

    # TODO wrap this in a try statement to catch invalid inputs

    if file_select == "all":
        file_list = child_list[1::]
    else:
        file_list = [child_list[int(file_select)]]

    return file_list

if __name__ == "__main__":
    # execute only if run as a script
    browse_dir()
    select_files()