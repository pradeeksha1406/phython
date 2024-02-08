import os
folder_list = input("please provide the list of folders names with space between them:= ").split()

for folder_list in folder_list:

    try:
     file = os.listdir(folder_list)
    except FileNotFoundError:
     print("please provide a valid folder name, looks like it doesn`t exist:=" + folder_list)
     break
    except PermissionError:
     print("you don`t have sudo permission to access this folder:=" + folder_list )
     break
    print("====listing files for the folder:=" + folder_list)
    for files in file:
     print(files)