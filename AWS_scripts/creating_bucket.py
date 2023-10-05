import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create the bucket with the specified location constraint
s3.create_bucket(Bucket='tech254-samiha-bucket', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

#printing back an output message to show it was successful.
print("Creation of bucket was successful!")