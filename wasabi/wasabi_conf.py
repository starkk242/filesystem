import boto3
import os

def get_bucket():
        for bucket in s3.buckets.all():
                return (bucket.name)	#To get the name of the bucket in s3 

def send_file(file_name,file_dir):
        s3.Object(bucket_name,file_name).upload_file(Filename=file_dir)	#To uploade file in s3

def create_folder(folder_name):
        s3.Bucket(bucket_name).put_object(Key=(folder_name+'/'))	#To create Folder in s3


s3 = boto3.resource(
    service_name='s3',
    endpoint_url = 'https://s3.eu-central-1.wasabisys.com',
    aws_access_key_id='7FMNYNLSLR5G6B2VT8U6',
    aws_secret_access_key='4rR9rzGah2tjnZHG5sCpMSm6vHzXDWVF7uUPKziw'
)	#s3 Configuration

bucket_name=get_bucket()
#print(bucket_name)
