### Steps to Create an EC2 Instance
1. Sign in to the AWS Management Console
Go to the AWS Management Console and sign in with your AWS account credentials.


2. Navigate to Amazon EC2
Amazon Elastic Compute Cloud (EC2) is the AWS service for creating instances. Click on "Services" in the top-left corner, and then select "EC2" under the "Compute" section.


3. Launch an Instance in the EC2 Dashboard, click "Launch Instance."

#### Launching an Instance

1. create a name for the instance so that it can be easily identified. 

![alt text](name_tags.png)

2. Select an AMI based on your requirements. You can choose from various operating systems and pre-configured software. 

![alt text](AMI.png)

3. Select an instance type based on your resource requirements (CPU, RAM, storage, etc.). AWS offers a variety of instance types optimized for different workloads.

![alt text](instant_type.png)

4. Select the key pair

![alt text](key_pair.png)

5. Configure Instance Details: Set options like the number of instances, network settings, and IAM roles if needed.

![alt text](security.png)

6. Configure Security Group: Create or select a security group to control inbound and outbound traffic to your instance.
![alt text](security.png)

7. Specify the size and type of storage (EBS volumes) for your instance.

![alt text](storage.png)


8. Review your instance configuration and click "Launch."

![alt text](summary.png)

### Deploying nginx webserver 

1. The instance has now successfully launched. We can now connect by pressing connect.

![alt text](connect.png)

2. You will be then given a set of instructions to connect using SSH client..

![alt text](ssh.png)

3. You are now ready to open Gitbash terminal and login.


4. Open the terminal and enter the command `cd .ssh`

![alt text](step1.png)


5. Enter the next command as instructed.

![alt text](step2.png)

6. After following all instructions, you will now be logged in. 

![alt text](login.png)

7. Enter the following commands in the following order

```
sudo apt update
sudo apt upgrade -y
sudo apt install nginx -y
sudo systemctl start nginx
```

8. Return to your AWS instance page and you will be able to locate your public IP address and launch your nginx webserver. 

![alt text](final.png)

![alt text](nginx.png)