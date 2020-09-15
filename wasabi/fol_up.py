import wasabi_conf

#file_name=input("Enter the name of the file that should be in s3")
#file_dir=input("Enter the directory of the file")

choice=input("Want to insert a file in s3 press F or for a Folder/Directory press D: ")

if(choice=='F' or choice=='f'):
	file_name=input("Enter the name of the file that should be in s3: ")
	file_dir=input("Enter the directory of the file: ")
	wasabi_conf.send_file(file_name,file_dir)
elif(choice=='D' or choice=='d'):
	folder_name=input('Enter folder name for s3')
	if(folder_name != ''):
		wasabi_conf.create_folder(folder_name)
	dir_path=input('Enter the path of the directory/folder: ')
