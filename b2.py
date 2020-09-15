import boto3

s3 = boto3.resource('s3',
endpoint_url = 'https://s3.eu-central-03.backblazeb2.com',
aws_access_key_id = '385638e80333',
aws_secret_access_key = '00358e6d6a3038b59e88ff664f547581ff5e6517b0')

s3.create_bucket(Bucket='starkk24625746')
