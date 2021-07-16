import os
import shutil

# check if file exists

# path = "C:\\Users\\OS\\Desktop"
# 
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exists")


path = "C:\\Users\\OS\\Desktop\\file.txt"

# read a file

#
# try:
#     with open(path) as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found.")


# write a file

# text = "Have a nice day!"
# with open(path, 'w') as file:
#     file.write(text)


# copy a file
# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

# shutil.copy2(path, "C:\\Users\\OS\\Desktop\\copy.txt")


# move a file

# source = "move.txt"
# destination = "C:\\Users\\OS"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " was found")
# except FileNotFoundError:
#     print(source + " was not found")


# delete a file

