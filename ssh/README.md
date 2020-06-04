# SSH
## Setting up credentials JSON database
This scripts allow you to connect to any device which credentials you saved. In order to save device credentials, proceed with the following command:

    $ ./insert_entry [target] [username] [IP] '[password]' [is_pem]

 - `target` - name of the new credentials entry, should be unique. It is used as an identificator for each credentials set
 - `username` - your username on the device
 - `IP` - IP of the device
 - `password` - password, should be enveloped in singular quotes to avoid bash errors. Moreover, if you use .pem keyfile to log in, you can save it into `pem` folder and specify its name here (without .pem extension) + set `is_pem` argument to `true`
 - `is_pem` - optional argument, should be set to `true` if a .pem keyfile is used
 
 ## Logging in
 

    $ ./connect [target]
It's that simple, yes. If you have already saved your credentials using the steps above, then you should be able to select the target you saved and connect to it using this command.

