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


6. You have now successfully created 2 subnets within your VPC 

![alt text](v10.png)

