### Nginx Reverse Proxy

#### What are ports? 

A port is a communication endpoint. It's like a door through which information flows to and from a computer. 

Ports are identified for each protocol and address combination by a 16-bit number, commonly known as the port number.

#### What is a reverse proxy? How is it different to a proxy? 

A **proxy** acts as an intermediary between a user and the internet. It intercepts requests and forwards them, masking the user's IP address.

A **reverse proxy**, on the other hand, sits between web servers and users. It handles requests from users, forwards them to web servers, then sends back the servers' responses to users. 


#### What is Nginx's default configuration (hint - 'sites-available' directory)

In Nginx, the default configuration for sites is usually stored in the sites-available directory. 

This configuration includes settings for how Nginx should handle different websites, including server blocks (similar to virtual hosts in Apache) specifying server names, ports, and file paths.

#### How do you set up a Nginx reverse proxy?

`sudo apt-get update`

`sudo apt-get install nginx`

`cd /etc/nginx/sites-available/`

`sudo nano default`

```
proxy_pass http://<<public_IP_address>>:3000;
proxy_set_header Host $host; 
proxy_set_header X-Real-IP $remote_addr;

```

`sudo systemctl restart nginx`