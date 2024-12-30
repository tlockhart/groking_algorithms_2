from os import listdir
from os.path import isfile, join

# Mnuemonic: Quincy and Greg may list popular cafes if service or quality is amazing.
def printnames(dir):
    # Loop through every file and folder in the current folder
    # listdir(dir): Returns a list of the names of all entries 
    # (files, folders) in the directory specified by dir
    
    # sorted: The sorted() function arranges the names of the 
    # entries in alphabetical order
    for file in sorted(listdir(dir)):
        # print("check file:", file)
        
        # Combines the directory path (dir) and file, with the 
        # correct seperator depending on OS
        fullpath = join(dir, file)
        # if it is a file print out the name
        if isfile(fullpath):
            print(file)
            # If it is a folder, call the function recursively to look for files and folders
        else:
            # Recursive Call
            printnames(fullpath)

printnames("pics")