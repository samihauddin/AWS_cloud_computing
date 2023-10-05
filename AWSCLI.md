## S3 Buckets using AWS CLI

Step 1: Launch EC2 <br>
Step 2: Connect instance on Git Bash
Step 3: Run the following commands:

```
sudo apt update
sudo apt upgrade -y
sudo apt install python -y
sudo apt install python-pip -y
sudo pip install awscli
aws configure
```
Step 4: Enter the following credentials:

- AWS Access Key ID [None]:
- AWS Secret Access Key [None]:
- Default region name [None]: `eu-west-1`
- Default output format [None]: `json`

Step 5: Check connection 
`aws s3 ls`

### Creating a bucket

```
aws s3 mb s3://<bucketnamehere> --region eu-west-1

make bucket: <bucketnamehere>
```

### Uploading a file to a bucket

```
aws s3 cp <file.name> s3://<bucketnamehere>

```
### Download a file from a bucket
```
aws s3 sync s3://<bucketname> <folder to download into>
```
### Delete from a bucket

```
aws s3 rb s3://<bucketname>
```