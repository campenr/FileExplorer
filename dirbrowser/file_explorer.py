# Copyright 2015 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Module that enables basic file/direcotry explorer functionality.

file_explorer version 0.1b
==========================

This module includes a number of functions that provide basic file
explorer functionality in an easy to view format within a command 
line environment, e.g. Windows shell. Using the two main functions
browse_dir() and select_files() in combination allows the user
to browse the directory tree and set a working directory, and return
a list of files within that directory, optionally filtered by file
type. This list of files can then be utilised by other scripts.

See README.txt for full documentation.
"""

import os

def list_children(directory, filter_type="none"):
    """Create a list of the children in 'directory'.

    Children in a directory are stored in a list, which can be filtered
    to contain only files or directories. Function returns a list of
    file and/or directory names. Valid filter_type arguments are:

    'none'  - Does not filter children. Deafult option.
    'file'  - Filter only allows files
    'dir'   - Filter only allows directories
    """

       
    # Get the list of children in the current directory, filtered
    # according to filter_type
    if filter_type == "none":
        child_list = os.listdir(directory)
    elif filter_type == "file":
        child_list = [child for child in os.listdir(directory)
                      if os.path.isfile(child)]
    elif filter_type == "dir":
        child_list = [child for child in os.listdir(directory)
                      if os.path.isdir(child)]
            
    # If an incorrect filter_type is entered the deafult 'none' is
    # selected and a message printed to notify user
    else:
        print("Invalid filter selected, deafult of 'none' chosen")
        child_list = os.listdir(directory)
 
    return child_list

def filter_file_type(file_list, file_type):
    """Filter a list of files by 'file type'.

    Filters a list of files according to file_type, which is a string
    that matches the file suffix e.g. txt, doc, jpg, py.
    """

    # Create new file_list by iterating over old file_list and only
    # including files that have ends matching the given file_type
    file_list = [file for file in file_list
                 if file.endswith(file_type)]
    
    return file_list

def user_input_file_type(file_list):
    """Implement filter_file_type with user input file_type.

    """

    # Prompt user to input file type to filter
    file_type = input("Enter file type to filter: ")

    # Create new file_list filtered by user specified file_type
    file_list = filter_file_type(file_list, file_type)

    return file_list

def create_child_dict(child_list, show_parent=True):
    """Build a dicitonary of child object values, and numeric keys.

    Iterate over child_list, combie with an incrementing integer
    using enumerate, and store in a dictionary object. If show_parent
    is set to True the child_list is prepended with '...' as a
    placeholder for the parent direcotry.
    """

    # If show_parent is true, prepend child_list with the parent place
    # holder string '...'
    if show_parent: child_list.insert(0, "...")

    # Generate dictionary from enumerating child_list
    child_dict = dict(enumerate(child_list))
    
    return child_dict

def display_children(child_dict):
    """Print child_dict in an easy to read format.

    Takes the child_dict dictionary object returned by the create_child
    _dict() function and displays the children ordered numerically by
    their keys in an easy to read manner, i.e:

    [0] ...
    [1] Folder1
    [2] File1.py
    [3] File2.txt
    [4] Folder2
    """
 
    # Create a sorted list of the keys from the child dictionary
    child_key_list = sorted(child_dict.keys())
               
    # Print each key/value pair in an easy to read manner
    for n in child_key_list:
        print("[{}] {}".format(child_key_list[n], child_dict[n])) 

    return

def change_dir():
    """Change the current working directory to a child/parent directory.
 
    This function is intended to operate within a loop provided by
    another function, browse_dir().

    Displays the current working dictionary, and then displays the
    children in the current working directory (files and directories).
    User is prompted to select a new directory by entering the assosiated
    number. The function returns user input as dir_number.

    An additional option of 'X' is used to confirm the current directory
    by returning False, discontinuing the loop in the funciton
    browse_dir() that change_dir is called in.
    """

    # Obtains and prints the current working directory, and prints the
    # children by calling the list_children() function
    current_dir = os.getcwd()
    print(current_dir)
    child_list = list_children(current_dir)
    child_dict = create_child_dict(child_list)
    display_children(child_dict)
    
    # Collect input from user to change the directory
    dir_number = input("Enter a number to select the corresponding "
                        "directory, or 'X' to confirm current "
                        "directory: ")

    # Change the directory according to user input
    if dir_number == "0":
        os.chdir(os.path.dirname(current_dir))
    elif dir_number == "X" or dir_number == "x":
        dir_number = False
    else:
        sub_dir = child_dict[int(dir_number)]
        os.chdir(os.path.join(current_dir, sub_dir))
        
    return dir_number


def browse_dir():
    """Loop change_dir() to browse directory tree, and catch exceptions.

    Loops change_dir(), checking the output each time that dir_number is
    True. If False the loop is terminated. This funciton catches any
    exceptions encountered by change_dir() while attempting to change
    the directory.
    """

    # Generate loop to repeatedly request user to change directory while
    # checking the output of change_dir() and continuing loop while True
    # and catching exceptions
    while True:
        try:
            dir_number = change_dir()
            if not dir_number:
                print(("\nSelected working directory is {}\n")
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

def select_files(file_list):
    """Generate a list of files as specified by user input.

    Files are selected by their number assosiated in the child_dict
    object.

    To implement:
    - Enable selecting a subset of files instead of simply all or one
    """
    
    # Generate child_dict object with create_child_dict funciton from
    # the file_list and display with display_children()
    child_dict = create_child_dict(file_list, show_parent=False)
    display_children(child_dict)

    # Prompt user to input files to select
    file_select = input("Select a file using the assosiated number, or"
                        " 'all' to select all files: ")

    # Splice file_list according to user input and return a new list
    if file_select == "all":
        file_list = file_list
    else:
        file_list = [file_list[int(file_select)]]

    return file_list

