import wasabi_conf

bucket = wasabi_conf.s3.Bucket(wasabi_conf.bucket_name)
prefix = ""

FilesNotFound = True
for obj in bucket.objects.filter(Prefix=prefix):
     print('{0}:{1}'.format(bucket.name, obj.key))
     FilesNotFound = False
if FilesNotFound:
     print("ALERT", "No file in {0}/{1}".format(bucket, prefix))

