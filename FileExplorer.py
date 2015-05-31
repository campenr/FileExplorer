import os

"""Program that performs basic file explorer functionality.

Program allows setting of current working directory, and listing of files/sub-
directories in current directory. Files listed in the directory can be filtered
by file type. Files/sub-directories are given a correspoding number allowing
selection of a file using a number. Funciton returns a list of files (in the
case of only wanting to select a single file the list is 1 item long).
"""
     

def list_children():
    """Function prints a list of all children in the current directory.

    Children include files and sub-directories assosiated with a number. 
    Children are stored in a dicitonary and assinged a numeric value. The
    zero value is set as '...' by default, as a placeholder for the parent dir.
    """

    #Initialise dictionary containing '...' as placeholder for parent dir
    child_dict = dict({0: "..."})
    
    #Get the list of children in the current working directory
    dir_list = os.listdir(os.getcwd())

    #Iterate over the list of children and add to the children dictionary
    #setting the key as the file/folder name and incrementing the value
    n = 1
    for i in dir_list:
        child_dict[n] = i
        n += 1
        
    #Create sorted lists of the keys from the children dictionary
    children_key_list = sorted(child_dict.keys())
        
    #Print each key/value pair in an easy to read manner
    for n in range(len(children_key_list)):
        print("[{}] {}".format(children_key_list[n], child_dict[n])) 


    #Return the dictionary of file/folder name keys and number value pairs
    return child_dict


def change_dir():
    """Function that can change to a selected directory.

    Can change to the parent of the current directory, or to a sub directory
    by selecting the assosiated number generated by list_children().
    """

    #Obtains and prints the current working directory, and prints the children
    #using list_children()
    current_dir = os.getcwd()
    print(current_dir)
    child_dict = list_children()
    
    #Collect input from user to change the directory
    new_dir_number = input("Enter a number to select the corresponding directory: ")

    #Change the directory
    #If 0 was selected change directory to parent directory
    if new_dir_number == "0":
        os.chdir(os.path.dirname(current_dir))

    #If a value other than 0 selected change to the specified directory or catch
    #exceptions caused by invalid choices
    else:
        try:
            sub_dir = child_dict[int(new_dir_number)]
            os.chdir(os.path.join(current_dir, sub_dir))
        except NotADirectoryError:
            print("{} is not a valid directory".format(child_dict[int(new_dir_number)]))
        except ValueError:
            print("Not a valid selection")
        except KeyError:
            print("Not a valid selection")
        except PermissionError:
            print("Insufficient permissions. Try running as administrator")
    return


while True:
    change_dir()
        
    
