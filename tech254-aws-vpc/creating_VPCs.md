## What are Virtual Private Clouds (VPCs)?

**VPC stands for Virtual Private Cloud.** 

A VPC is a virtual network dedicated to your AWS account. It enables you to launch AWS resources into a virtual network that you've defined. 

When you create a VPC, you specify its private IPv4 address range (in the form of a CIDR block, such as 10.0.0.0/16), create subnets, configure route tables, and configure security settings.

#### Diagram displaying VPCs

![alt text](diagram1.png)

## Setting up Virtual Private Clouds (VPCs) in AWS

### Step 1: Sign into AWS Concole

- Go to the AWS Management Console. <br>
- Sign in with your AWS account credentials.

### Step 2: Creating a VPC

1. Search for VPC on your AWS console, Navigate to `Your VPCs`

![alt text](v1.png)

2. Then press `create VPC`

![alt text](v2.png)

3. Fill in the details to `Create VPC`
- Select `VPC only`
- Create an identifiable name tage e.g `tech254-samiha-2tier-first-vpc`
- IPv4 CIDR block - keep as default 
- Input IPv4 CIDR `10.0.0.0/16`

![alt text](v3.png)

4. Tags: these are pre-filled, then press `create`

![alt text](v4.png)

5. You have now successfully created a VPC

![alt text](v5.png)

### What are Subnets?

Subnets are subdivisions of your VPC's IP address range, and resources are launched inside these subnets. 

Subnets help in organizing resources, improve security by providing segmentation, and allow for high availability by placing resources in different availability zones. Subnets are contained within a VPC and cannot exist outside of it.

### Step 3: Creating Subnets

1. Navigate to `Subnets`

![alt text](v6.png)

2. Select the VPC that you have created 

![alt text](v7.png)

3. Within the VPC we much create 2 subnets. A public subnet and a private subnet.

Fill in the details of your public subnet 
- `Subnet name`
- `Availibility Zone`
- Enter IPv4 VPC CIDR block `10.0.2.0./24`
- Tags - these are pre-filled

![alt text](v8.png)

4. Fill in the details of your private subnet 
- `Subnet name`
- `Availibility Zone`
- Enter IPv4 VPC CIDR block `10.0.3.0./24`
- Tags - these are pre-filled

![alt text](v9.png)

5. Then press `Create subnet`


6. You have now successfully created 2 subnets within your VPC. 

![alt text](v10.png)

### Step 4: Creating an Internet Gateway

1. Navigate to`Internet Gateway`

![alt text](ig1.png)

2. Select `Create Internet Gateway` 

![alt text](ig2.png)

3. Create a Name tag e.g. `tech254-samiha-2tier-first-vpc-ig`

![alt text](ig3.png)

4. Then select `Create internet gateway `

5. Your internet gateway has now been created, now **we must attach it to the VPC**.

- Click *Actions* > `Attach a VPC`

![alt text](attach.png)

6. Search for your VPC and select `Attach to Internet Gateway`

![alt text](attach2.png)

### Step 5: Creating a Route table

1. Navigate to Route Tables

![alt text](rt.png)

2. Create Route Tables
- Create a Name e.g `public-rt`
- Then select your VPC from the dropdown

![alt text](rt1.png)

4. Then select `Create Route Table`

You have now successfully created route table.

### Step 6: Creating Association

5. Navigate to `Subnet Association`

![alt text](subnet.png)

6. Click `Edit Subnet Association`

7. Check the `puclic-subnet` option

![alt text](check.png)

![alt text](s1.png)

### Connecting your internet gateway to your route table
- `Edit Routes`
- `Add Route`
- `Enter destination: 0.0.0.0./0`
- `Target:` select you internet gateway
- Select `create`

8. You can now test your pathway by navigating to your resource map in Internet gateway.

![alt text](testing.png)

### Step 7: Creating your Virtual Machines

#### Creating your Database Instance

1. Navigate to AMIs in EC2. 
2. Search for your AMI and select this
5. Then select `Launch Instance from AMI`

Launching your instance

1. Name = `tech254-samiha-db-test-first-vpc`
5. Key pair = tech254
6. Network settings > Edit settings 
7. VPC > select your VPC 

![alt text](vp1.png)

8. Subnet: Select `private-subnet`
9. Select `disable`

10. Create security Group
![alt text](csg.png)
![alt text](sg.png)
11. Fill in MongoDB security using the following:
![alt text](mongo.png)

12. Then review the configurations and select `Launch Instance`

#### Creating your App Instance

1. Navigate to AMIs in EC2. 
2. Search for your AMI that contains the app. 
5. Then select `Launch Instance from AMI`

Launching your instance

1. Name = `tech254-samiha-app-test-first-vpc`
5. Key pair = tech254
6. Network settings > Edit settings 
7. VPC > select your VPC 
![alt text](vp1.png)
8. Subnet: Select `public-subnet`
9. Select `enable`

![alt text](enable.png)

10. Create security Group
![alt text](create.png)
11. Create Security Rules as the following:
![alt text](sg3.png)

12. Then navigate to `User Data`
- Then enter the following commands 

```
#!/bin/bash

export DB_HOST=mongodb://private_IP_of_DB_instance:27017/posts

cd /home/ubuntu/repo/app
sudo systemctl restart nginx
npm install
node seeds/seed.js
sudo npm install pm2 -g

pm2 kill
pm2 start app.js
```
![alt text](ud1.png)

3. Select `Launch Instance`
4. Navigate to you app instance and copy and paste the public IP address. This should load the app page. 

![alt text](app.png)

5. In the url after the IP address enter `/posts`
- This should navigate you to the data page 

![alt text](posts.png)