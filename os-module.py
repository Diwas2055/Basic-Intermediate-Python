import os

""" Handling the Current Working Directory """

# ! Getting the current working directory.
os.getcwd()

# ! Changing the current working directory to the parent directory.
os.chdir('../')
 
""" Joining the path """ 

# ! os.path.join() Joining the parent directory and the directory to create a path.
def join_path():
        # Directory
        directory = "GeeksforGeeks"
        
        # Parent Directory path
        parent_dir = "D:/Pycharm projects/"
        
        return os.path.join(parent_dir, directory)    
    
""" Creating a Directory in Python """
    
# ! os.mkdir() method in Python is used to create a directory 
# named path with the specified numeric mode. 
# This method raises FileExistsError if the directory to be created already exists.
os.mkdir(join_path())


# ! os.makedirs() method in Python is used to create a directory recursively.
# That means while making leaf directory if any intermediate-level directory 
# is missing, os.makedirs() method will create them all.
os.makedirs(join_path())

""" Listing out Files and Directories with Python """

# ! Get the list of all files and directories in the root directory
path = "/"
os.listdir(path)

""" Deleting Directory or Files using Python """

# ! os.remove() method in Python is used to remove or delete a file path. 
# This method can not remove or delete a directory. 
# If the specified path is a directory then OSError will be raised by the method.
def remove ():
    file = 'file.txt'
    location = "D:/Pycharm projects/Authors/"
    path = os.path.join(location, file)       
    # Remove the file
    # 'file.txt'
    os.remove(path)
    
# ! os.rmdir() method in Python is used to remove or delete an empty directory. 
# OSError will be raised if the specified path is not an empty directory.    
def remove_dir():
    directory = "Geeks"
    parent = "D:/Pycharm projects/"        
    # Path
    path = os.path.join(parent, directory)        
    # Remove the Directory
    # "Geeks"
    os.rmdir(path)

""" Commonly Used Functions """

# ! os.path.exists(): This method will check whether a file exists or 
# not by passing the name of the file as a parameter. 
# OS module has a sub-module named PATH by using which 
# we can perform many more functions. 
os.path.exists("file_name") # // giving the name of the file as a parameter.


# ! Returning the size of the file in bytes.
os.path.getsize("filename")
    
