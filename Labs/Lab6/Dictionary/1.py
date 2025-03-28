import os
path=input("Input specified path:")
print("Files in specified folder are :",os.listdir(path))
#1)
files = []
for f in os.listdir(path):
    full_path = os.path.join(path, f)  
    if os.path.isfile(full_path):  
        files.append(f) 
print("Файлы в папке:", files)  
#2)
directories=[]
for d in os.listdir(path):
    full_path=os.path.join(path,d)
    if os.path.isdir(full_path):
        files.append(d)
print("директорий в папке:", directories)  
