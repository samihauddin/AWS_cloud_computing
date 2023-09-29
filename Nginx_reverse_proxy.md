### Nginx Reverse Proxy

#### What are ports? 

A port is a communication endpoint. It's like a door through which information flows to and from a computer. Ports are identified for each protocol and address combination by a 16-bit number, commonly known as the port number.

#### What is a reverse proxy? How is it different to a proxy? 

**Proxy:**
A proxy server acts as an intermediary between a client and a destination server. It receives requests from clients seeking resources from other servers and forwards those requests to the destination servers. The destination servers respond to the proxy, which, in turn, sends the response to the client.

**Reverse Proxy:**
A reverse proxy is similar to a regular proxy but operates in the opposite direction. It receives requests from servers seeking resources and forwards those requests to the appropriate clients. When clients respond, the reverse proxy sends the response back to the servers.

#### Make a diagram for the above point to go with your explanation

#### What is Nginx's default configuration (hint - 'sites-available' directory)

Nginx's default configuration is stored in the sites-available directory. In this directory, you can find configuration files for different sites or applications hosted on the Nginx server. These configuration files contain settings such as server names, listening ports, and proxy configurations.

#### How do you set up a Nginx reverse proxy?