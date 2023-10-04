## App and MongoDB Deployment 

### Step 1: Launching the app

1. Sign in to AWS Management Console: Sign into your AWS and and go to the EC2 dashboard. 
2. Click on 'Launch Instance'
3. Choose an My AMIs, select and instance type, configure instance details and add storage if needed.
4. Configure security groups and then launch the instance. 
5. Navigate to the Linux terminal and connect as usual. 
6. Check the write version is installed.

### Step 2: Launching the DB instance.

2. Click on 'Launch Instance'
3. Choose an AMI, select and instance type, configure instance details and add storage if needed.
4. Configure security groups and a new custom security group, change port number. 
5. Navigate to another Linux terminal and connect as usual. 

### Step 3: Install MongoDB

`sudo apt update`

`sudo apt upgrade -y`

`wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -`

`echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list`

`sudo apt update`

`sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20`

`sudo nano /etc/mongod.conf`

Edit the MongoDB configuration file and change the 'bindIp' option to your server's public IP address.

`0.0.0.0`

` sudo systemctl mongod start mongod`

`sudo systemctl enable mongod`

`sudo systemctl status mongod`

### Step 4: Connecting the application to MongoDB

`export DB_HOST=mongodb://<app ip address>:27017/posts`

`ls`

`cd app`

`npm install`

`node app.js`

Return to IP address enter :3000/posts


