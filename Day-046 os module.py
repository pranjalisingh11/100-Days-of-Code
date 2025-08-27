# firstly we have to go on vscode and then create a main.py file and then run a code and then it will give you a
#   directory name data then inside it, there will be 100 folders

#main.py
import os

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i + 1}")

#oslist.py -> to show a full list of folders of data
import os
folders = os.listdir("data")

print(os.getcwd())       #-> to check the name of exisiting directory
os.chdir("/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

#rename.py  -> to rename the folders
import os

for i in range(0, 100):
    os.rename(f"data/Tutorial{i + 1}", f"data/Tutorial {i + 1}")