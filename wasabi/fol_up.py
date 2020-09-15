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
	os.chdir('../')
	return(files)

path='../../file1'
path_1='~/'
name_folder_s3='file1'
folders=folder_list(path)
wasabi_conf.create_folder(name_folder_s3)
curr_dir_s3=name_folder_s3

for i in folders:
	files=[]
	curr_dir_s3=name_folder_s3
	curr_dir_s3=curr_dir_s3+'/'+i
	if curr_dir_s3!=name_folder_s3+'/.':
		wasabi_conf.create_folder(curr_dir_s3)
	files=file_list(i)
	for j in files:
		print('dir = '+i)
		if curr_dir_s3==name_folder_s3+'/.':
			curr_dir_s3=name_folder_s3
		print('file_dir = '+curr_dir_s3+'/'+j,'./'+j)
		wasabi_conf.send_file(curr_dir_s3+'/'+j,path_1+curr_dir_s3+'/'+j)
	#wasabi_conf.create_folder()


#for i in subfolders_name
#wasabi_conf.send_file(file_name,file_dir)

#wasabi_conf.create_folder(folder_name)
