import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-samiha-bucket'
filename = 'example.txt'
s3_file_name = 'example.txt'

s3.upload_file(filename, bucket_name, s3_file_name)

print("file has been successfully uploaded!")