import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-samiha-bucket'
s3_file_name = 'example.txt'
download_name = 'download_file_example.txt'

s3.download_file(bucket_name, s3_file_name, download_name)

print("file has been successfully downloaded!")
