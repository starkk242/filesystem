import os

files=[]

subfolders = [ f.name for f in os.scandir('../fsociety') if f.is_dir() ]
print(subfolders)

print('**************************************************')

with os.scandir('../fsociety') as it:
    for entry in it:
        if entry.is_file():
            files.append(entry.name)
print(files)
#arr = os.listdir('../')
#print(arr)
