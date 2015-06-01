import os

current_dir = os.getcwd()
print(current_dir)

os.chdir(os.path.dirname(current_dir))

current_dir = os.getcwd()
print(current_dir)

f = input()
