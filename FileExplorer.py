"""Program that performs basic file/direcotry explorer functionality.

Program allows setting of current working directory, and listing of
files/folder children in current directory. Children are stored in a
dicitonary object and given a correspoding number allowing selection
of a file/folder using the number.
"""

import os

def find_children(directory, child_filter=False,
                  filter_type="none"):
    """Create a dicitonary of names of children in a directory.

    Children in the directory are stored as values in the dictionary
    and are assinged a non-zero positive integer as a key. Children
    include files and folders. The 0 key is assinged to '...' which
    acts as a placeholder for the parent directory. Returns the
    child_dict dictionary object. The directory is set as the current
    working directory by default, using os.getcwd().
    
    -Implement the following:
    
    Children can be filtered by setting the child_filter argument to
    True, the default is False. If filtering is selected the filter_type
    argument must be set, it's default is none. The valid filter_type
    arguments are:

    none   - does not filter the children (default)
    file   - filters to show only children that are files
    folder - filters to show only children that are folders
    """

    #Initialise dictionary
    child_dict = dict({0: "..."})
    
    #Get list of all children in current working directory if child_filter
    #is False, or filter_type set as 'none'.
    if not child_filter or filter_type == "none":
        dir_list = os.listdir(directory)
        
    #Get the list of children in the current working directory, filtered
    #according to filter_type if child_filter is True    
    elif child_filter:

        #Filters out folders
        if filter_type == "file":
            dir_list = [child for child in os.listdir(directory)
                        if os.path.isfile(child)]

        #Filters out files    
        elif filter_type == "folder":
            dir_list = [child for child in os.listdir(directory)
                        if os.path.isdir(child)]
            
        #If an incorrect filter type is entered the deafult is selected
        #and a message printed to notify user
        else:
            print("Invalid filter selected, deafult of 'none' chosen")
            dir_list = os.listdir(directory)
 
    #Iterate over the list of children and add to the child-dict object
    #setting the value as the file/folder name and incrementing the key
    n = 1
    for child in dir_list:
        child_dict[n] = child
        n += 1

    return child_dict

def display_children():
    """Print the child_dict in an easy to read format.

    Takes the child_dict dictionary object returned by the find_children()
    function and displays the children ordered numerically by their keys
    along with the parent directory placeholder '...', in an easy to read
    manner,  i.e.

    [0] ...
    [1] child_1
    [2] child_2
    """
     
    #Create a sorted list of the keys from the child dictionary
    child_key_list = sorted(child_dict.keys())
            
    #Print each key/value pair in an easy to read manner
    for n in child_key_list:
        print("[{}] {}".format(child_key_list[n], child_dict[n])) 

    #Return list of children
    return list(child_dict.values())


def change_dir():
    """Change the current working directory to a child/parent directory.
 
    This function is intended to operate within a loop provided by
    another function, browse_dir().

    Displays the current working dictionary, and then displays the
    children in the current working directory (files and folders) using
    display_children. User is prompted to select a new directory by
    entering the assosiated number. The function returns user input as
    new_dir_number.

    An additional option of 'X' is used to confirm the current directory
    by returning False, discontinuing the loop in the funciton browse_dir()
    that change_dir is called in.
    """

    #Obtains and prints the current working directory, and prints the
    #children by calling the list_children() function
    current_dir = os.getcwd()
    print(current_dir)
    child_dict = find_children(current_dir)
    display_children(child_dict)
    
    #Collect input from user to change the directory
    new_dir_number = input("Enter a number to select the corresponding "
                           "directory, or 'X' to confirm current "
                           "directory: ")

    #Change the directory
    #If '0' selected change to the parent directory    
    if new_dir_number == "0":
        os.chdir(os.path.dirname(current_dir))
    #If 'X' or 'x' selected set new_dir_number to False
    elif new_dir_number == "X" or new_dir_number == "x":
        new_dir_number = False
    #If a value other than 0 selected change to the specified directory
    else:
        sub_dir = child_dict[int(new_dir_number)]
        os.chdir(os.path.join(current_dir, sub_dir))
        
    return new_dir_number


def browse_dir():
    """
    Loop change_dir() while True to browse directory tree.

    Loops change_dir(), checking the output each time that new_dir_number
    is True. If False the loop is terminated. This funciton catches
    any exceptions encountered while attempting to change the directory.
    """

    #Generate loop to repeatedly request user to change directory while
    #checking the output of change_dir() and continuing loop while True
    while True:
        #Try to change the directory, and check if new_dir_number is
        #True. If new_dir_number is False loop terminates confirming the
        #current directory as the working directory.
        try:
            new_dir_number = change_dir()
            if not new_dir_number:
                print(("Selected working directory is {}").format(os.getcwd()))
                return new_dir_number
        #Exceptions encountered when changing directory are handled as below
        except NotADirectoryError:
            print("That is not a valid directory")
        except ValueError:
            print("Not a valid selection")
        except KeyError:
            print("Not a valid selection")
        except PermissionError:
            print("Insufficient permissions. Try running as administrator")
    return

browse_dir()
files = list(find_children(os.getcwd(), child_filter=True, filter_type='file').values())[1::]
print(files)



    
