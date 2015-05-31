import os
import tempfile

"""Program that performs basic file explorer functionality.

Program allows setting of current working directory, and listing of files/sub-
directories in current directory. Files listed in the directory can be filtered
by file type. Files/sub-directories are given a correspoding number allowing
selection of a file using a number. Funciton returns a list of files (in the
case of only wanting to select a single file the list is 1 item long).
"""
     

def dir_children():
    """Function returns a dictionary of all children in the current directory.

    Children include files and sub-directories assosiated with a number. The
    zero value is set as '...' by default, as a placeholder for the parent dir.
    """

    children = dict({"...": 0})

    current_dir = os.getcwd()

    dir_list = os.listdir(current_dir)

    n = 1
    for i in dir_list:
        children[i] = n
        n += 1
        
    children_key_list = sorted([i for i in children.keys()])
    children_value_list = sorted([i for i in children.values()])

    for n in range(len(children_key_list)):
        print("[{}] {}".format(children_value_list[n], children_key_list[n])) 


    return children


dir_children()

