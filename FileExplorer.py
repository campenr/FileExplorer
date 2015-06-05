"""Program that performs basic file/direcotry explorer functionality.

Program allows setting of current working directory, and listing of
files/directory children in current directory. Children are stored in a
dicitonary object and given a correspoding number allowing selection
of a file/folder using the number.
"""

import os

def list_children(directory, filter_type="none"):
    """Create a list of children in 'directory'.

    Children in a directory are stored in a list, which can be filtered
    to contain only files or directories. Function returns a list of
    file and/or directory names. Valid filter_type arguments are:

    'none'  - Does not filter children. Deafult option.
    'file'  - Filter only allows files
    'dir'   - Filter only allows directories
    """

       
    #Get list of all children in current working directory if
    #filter_type is set as 'none'.
    if filter_type == "none":
        child_list = os.listdir(directory)
        
    #Get the list of all files in the directory if filter_type set
    #as 'file'
    elif filter_type == "file":
        child_list = [child for child in os.listdir(directory)
                      if os.path.isfile(child)]

    #Get the list of all folders in the directory if filter_type is set
    #as 'folder'    
    elif filter_type == "dir":
        child_list = [child for child in os.listdir(directory)
                      if os.path.isdir(child)]
            
    #If an incorrect filter_type is entered the deafult 'none' is selected
    #and a message printed to notify user
    else:
        print("Invalid filter selected, deafult of 'none' chosen")
        child_list = os.listdir(directory)
 
    return child_list

def filter_file_type(file_list, file_type):
    """Filter a list of files by 'file type'.

    Filters a list of files according to file_type, which is a string
    that matches the file suffix e.g. txt, doc, jpg, py.
    """

    #Create new file_list by iterating over old file_list and only
    #including files that have ends matching the given file_type
    file_list = [file for file in file_list
                 if file_type == (file[-(len(file_type))::])]
    
    return file_list

def create_child_dict(child_list, show_parent=True):
    """Build a dicitonary of child objects and numeric keys.

    Iterate over a list of child objects and add them to a dicitonary,
    assinging a numeric key. The numeric key starts at one and is
    incremented by one for each child object. The Zero key is added to
    represent the parent directory if show_parent is set to True.
    """

    #Initialize empty dictionary
    child_dict = {}

    #Add child objects to child_dict with nuemric keys
    if show_parent:
        child_dict[0] = "..."

    n = 1
    for child in child_list:
        child_dict[n] = child
        n += 1

    return child_dict

def display_children(child_dict):
    """Print child_dict in an easy to read format.

    Takes the child_dict dictionary object returned by the create_child
    _dict() function and displays the children ordered numerically by
    their keys in an easy to read manner, i.e:

    [0] ...
    [1] child_1
    [2] child_2
    """
 
    #Create a sorted list of the keys from the child dictionary
    child_key_list = sorted(child_dict.keys())
            
    #Print each key/value pair in an easy to read manner
    for n in child_key_list:
        print("[{0}] {1}".format(child_key_list[n], child_dict[n])) 

    return


def change_dir():
    """Change the current working directory to a child/parent directory.
 
    This function is intended to operate within a loop provided by
    another function, browse_dir().

    Displays the current working dictionary, and then displays the
    children in the current working directory (files and directories)
    using display_children(). User is prompted to select a new directory
    by entering the assosiated number. The function returns user input
    as dir_number.

    An additional option of 'X' is used to confirm the current directory
    by returning False, discontinuing the loop in the funciton
    browse_dir() that change_dir is called in.
    """

    #Obtains and prints the current working directory, and prints the
    #children by calling the list_children() function
    current_dir = os.getcwd()
    print(current_dir)
    child_list = list_children(current_dir)
    child_dict = create_child_dict(child_list)
    display_children(child_dict)
    
    #Collect input from user to change the directory
    dir_number = input("Enter a number to select the corresponding "
                        "directory, or 'X' to confirm current "
                        "directory: ")

    #Change the directory
    #If '0' selected change to the parent directory    
    if dir_number == "0":
        os.chdir(os.path.dirname(current_dir))
    #If 'X' or 'x' selected set new_dir_number to False
    elif dir_number == "X" or dir_number == "x":
        dir_number = False
    #If a value other than 0 selected change to the specified directory
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

    #Generate loop to repeatedly request user to change directory while
    #checking the output of change_dir() and continuing loop while True
    while True:
        #Try to change the directory, and check if new_dir_number is
        #True. If new_dir_number is False loop terminates confirming the
        #current directory as the working directory.
        try:
            dir_number = change_dir()
            if not dir_number:
                print(("Selected working directory is {}")
                      .format(os.getcwd()))
                return
        #Exceptions encountered when changing directory are handled as
        #below
        except NotADirectoryError:
            print("That is not a valid directory")
        except ValueError:
            print("Not a valid selection")
        except KeyError:
            print("Not a valid selection")
        except PermissionError:
            print("Insufficient permissions. Try running as "
                  "administrator")
    return

browse_dir()

