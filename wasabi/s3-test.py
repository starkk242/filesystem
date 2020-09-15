import boto3
import os

def get_bucket():
        for bucket in s3.buckets.all():
                return (bucket.name)

def send_file(file_name,file_dir):
	#s3.create_bucket(Bucket= bucket_name)
	s3.Object(bucket_name,file_name).upload_file(Filename=file_dir)

def upload_objects(path):

	for root,dirs,files in os.walk(path):
		for file in files:
			s3.upload_file(os.path.join(root,file),bucket_name,file)

s3 = boto3.resource(
    service_name='s3',
    endpoint_url = 'https://s3.eu-central-1.wasabisys.com',
    aws_access_key_id='7FMNYNLSLR5G6B2VT8U6',
    aws_secret_access_key='4rR9rzGah2tjnZHG5sCpMSm6vHzXDWVF7uUPKziw'
)

bucket_name=get_bucket()
print(bucket_name)

#file_name=input("Enter the name of the file that should be in s3")
#file_dir=input("Enter the directory of the file")

choice=input("Want to insert a file in s3 press F or for a Folder/Directory press D: ")

if(choice=='F' or choice=='f'):
	file_name=input("Enter the name of the file that should be in s3: ")
	file_dir=input("Enter the directory of the file: ")
	send_file(file_name,file_dir)
elif(choice=='D' or choice=='d'):
	dir_path=input('Enter the path of the directory/folder: ')
	upload_objects(dir_path)

else:
	print('The files are: ')


prefix = ""
bucket = s3.Bucket(name=bucket_name)
FilesNotFound = True
for obj in bucket.objects.filter(Prefix=prefix):
     print('{0}:{1}'.format(bucket.name, obj.key))
     FilesNotFound = False
if FilesNotFound:
     print("ALERT", "No file in {0}/{1}".format(bucket, prefix))
