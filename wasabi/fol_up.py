import os
import wasabi_conf

def folder_list(path):
	dir=path
	os.chdir(dir)
	subfolders_names = [ f.name for f in os.scandir('.') if f.is_dir() ]
	subfolders_names.append('.')
	#subfolders_dir = [ f.path for f in os.scandir('.') if f.is_dir() ]
	return(subfolders_names)

def file_list(path):
	dir=path
	os.chdir(dir)
	with os.scandir('.') as it:
		for entry in it:
			if entry.is_file():
				files.append(entry.name)
	return files





#for i in subfolders_name
#wasabi_conf.send_file(file_name,file_dir)

#wasabi_conf.create_folder(folder_name)
