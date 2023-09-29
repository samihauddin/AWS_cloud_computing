### App deployment using Nodejs

1. Launch your EC2 instance. Refer to notes on Github: https://github.com/samihauddin/AWS_cloud_computing/blob/main/launching_instances.md

2. Navigate to Gitbash and connect via SSH client. 

### Copying files into EC2 (scp -i Method)

Example 1:

`scp -i "<filepath to .pem file>" -r app ubuntu@ec2-3-250-0-59.eu-west-1.compute.amazonaws.com>`

Example 2:

`scp -i "C:/Users/Samiha/.ssh/tech254.pem" -r app ubuntu@ec2-34-242-237-25.eu-west-1.compute.amazonaws.com:~`


### Copying files into EC2 (Git Method)

`sudo apt install git -y`

`git clone https://github.com/LSF970/sparta_test_app.git`

### Installing Nodejs

Install the version of Nodejs you would like to use using the following command:

`curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -`

Proceed to install Node.js using the following command:

`sudo apt install nodejs -y`

`node -v`

Next, install PM2 globally, a process manager for Node.js applications:

`sudo npm install pm2 -g`

PM2 is installed using the Node Package Manager (npm) and manages application processes effectively.

### Deploying the app

**Navigate to Your Application Folder:**

Before proceeding with the final installation command, change directory to your application folder using the `cd` command:

`cd testing_scp_gitclone`

`cd app`

**Install Application Dependencies:**

Inside your application folder, install all required libraries and dependencies using the following command. This command installs all necessary libraries within the environment needed to run your application.

`npm install `

**Run Your Application:**

Finally, execute the following command while still in your application folder. This command launches your application, allowing it to run and be accessible.

`node app.js`

**Return to AWS Instance page:**

1. In AWS you need to add port range 3000 to inbound security group. 

2. Paste into the IP address with the port `:3000`

