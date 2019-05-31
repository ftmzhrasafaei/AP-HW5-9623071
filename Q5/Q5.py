import os
from pathlib import Path




def create_dir(name, address):
    #changing directory
    os.chdir(address)
    #path of name folder of this directory
    p = Path(name)
    #check for exsistance of path
    if p.exists():
        print(" exists ")
    else:
        #creating directory
        p.mkdir()



def create_file(name, address):
    #changing directory
    os.chdir(address)
    # open and close at the same time
    open(name, 'a').close()




def delete(name, address):
    #changing directory
    os.chdir(address)
    #path of name folder of this directory
    p = Path(name)
    #check for exsistance of path
    if p.exists():
        #checking that the name is a folder or file
        if name.find(".") != -1:
            #remove file
            os.remove(name)
        else:
            #remove folder
            p.rmdir()
            #print(" exists ")
    else:
        print("not exists ")




def find(name, address):
    files = []
    dirs=[]
    # all file and directories
    for (dirpath, dirnames, filenames) in os.walk(address):
        for f in filenames:
            #print(f)
            if f == name:
                files.append(os.path.join(dirpath, f))
        for d in dirnames:
            #print(d)
            if d == name:
                dirs.append(os.path.join(dirpath, d))

    if name.find(".") != -1:
        print(files)
        return files
    else:
        print(dirs)
        return dirs



cm = ["create_dir(name, address)" , "create_file(name, address)" , "delete(name, address)" , "find(name, address)"]
print("                          WELCOME ! \n")
print(" you can use these commands to create or delete a file or directory and find address of file or directory by entering name of file or dir and its address ! \n")
for c in cm:
    print(c)
command = input("        Enter the command: \n ")
exec(command)
