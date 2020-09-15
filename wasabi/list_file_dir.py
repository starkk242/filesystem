import os
import wasabi_conf

dir='../../fsociety'
os.chdir(dir)
files=[]

subfolders_names = [ f.name for f in os.scandir('.') if f.is_dir() ]
subfolders_dir = [ f.path for f in os.scandir('.') if f.is_dir() ]

print(subfolders_names)
print(subfolders_dir)

with os.scandir('.') as it:
    for entry in it:
        if entry.is_file():
            files.append(entry.name)
print(files)

#for i in files:
#	wasabi_conf.send_file
