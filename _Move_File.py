import os
import shutil

# source = "qwe.txt"
# destination = "C:\\Users\\OS\\Desktop\\qwe.txt"
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

path = "empty"
try:
    # os.remove(path)
    # os.rmdir(path)  # remove directory
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
