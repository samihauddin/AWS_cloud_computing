## PM2 Research 

#### **What is PM2?**

PM2 is a production-ready process manager for Node.js applications. It helps you manage and keep your application online, and it's packed with features that are useful for managing and monitoring Node.js processes in a production environment.

#### **Why is it useful?**

- **Keeps Applications Running:** PM2 ensures your Node.js apps are always up and running, even if they crash.

- **Automatic Restarts:** If an app crashes, PM2 restarts it automatically, minimizing downtime.

- **Log Management:** PM2 helps you keep track of your app's logs and errors, making troubleshooting easier.

- **Handles Traffic:** It can balance incoming traffic across multiple instances of your app, optimizing performance.

- **Easy Deployment:** PM2 allows seamless updates without disrupting the app's service, ensuring continuous operation.

#### **What are some of the commands we can use to interact with node processes?**

`pm2 start <app.js>`: Start a Node.js application.

`pm2 stop <app_name_or_id>`: Stop a running application.

`pm2 restart <app_name_or_id>`: Restart a running application.

`pm2 list`: List all running processes managed by PM2.

`pm2 monit`: Monitor CPU, memory usage, and other metrics for all running processes.

`pm2 logs`: Display logs for all processes.

`pm2 info <app_name_or_id>`: Display detailed information about a specific process.

`pm2 delete <app_name_or_id>`: Delete a process from PM2.

#### **How you can manage processes using PM2.**

**Start an App**: Use `pm2 start <app.js>` to launch your app.

**Scale Apps**: Run multiple instances with `pm2 start <app.js> -i <number_of_instances>`.

**Monitor Apps**: Check CPU and memory usage with `pm2 monit`.

**Handle Errors**: View logs using `pm2 logs` and manage errors effectively.

**Deploy Seamlessly**: Update your app without downtime using `pm2 pull <repository_url>` and `pm2 reload <app_name_or_id>`.