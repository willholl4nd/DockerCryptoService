# DockerCryptoService
## Table of Contents
1. [What is this project?](#what-is-this-project)
2. [Installation](#installation)
3. [Setup](#setup)
4. [Running the project](#running-the-project)

### What is this project?

This project is build off the stand-alone [CryptoService](https://github.com/willholl4nd/CryptoService)
that I initially built. I realized that the project had a large barrier to
entry (a few different libraries to install, manual postfix and database
setup), so I turned to Docker to containerize the project. This is my first
time messing around with Docker, so if you have any tips or comments, don't be
afraid to post an issue or pull request.

### Installation

I will keep this project updated with the main 
[CryptoService](https://github.com/willholl4nd/CryptoService) project, 
so you won't have to worry about version differences. 

Clone this repo into a directory where you want the project to live: <br>
```bash 
git clone https://github.com/willholl4nd/DockerCryptoService
cd DockerCryptoService
```

### Setup
There are a few things you must do to get this project working.

#### Inside the scripts folder
1. Edit the project.json file <br>

This is the file that will contain information about when you want the email sent out, 
and where to send the emails to. Any more customization in the file would require 
a database table addition and/or modification to other files. This is discussed in step 3.<br />

2. Edit the Dockerfile <br>

This file contains the build information for this custom image. There is a line
that changes the timezone. By default, it is US/Eastern. There are also packages apt 
is installing that are labeled as "maybe don't need" packages. If you don't think you'll 
ever need them, you can comment that line out. <br />

3. Edit the crypto.sql file <br>

These are the tables that are created in the *crypto* database by default. If you 
want to add more cryptocurrencies, you need to add the tables here with the same two
columns as the default tables. You also need to add the cryptocurrency symbol, table name
and price column name to the project.json file. This file also contains the timezone
for the database (defaults to US/Eastern).

**NOTE:** The cryptocurrency symbol must be compatible with the API we are using.

#### Outer directory

4. Edit the docker-compose.yml <br>

    * sqldata container: <br>

    MYSQL_ROOT_PASSWORD field directly maps to the password in the project.json 
    file. If you change it here, you have to change it there, and vice versa.

    MYSQL_DATABASE field directly maps to database in the project.json file. If 
    you change it here, you have to change it there, and vice versa.

    * scripts container: <br>

    SMTP_USERNAME field is the email you would like to send from.

    SMTP_PASSWORD field is the [generated app password](https://support.google.com/accounts/answer/185833?hl=en)
    from inside your gmail security settings. This is required for postfix to 
    redirect mail through gmail's SMTP servers.

### Running the project 
After the project is installed and setup, all you need to do is run:
```bash
docker-compose up
```
Everything should be in working order, and as long as you have an internet connection, 
this program should email you an overview of the prices of the cryptocurrencies 
you choose along with a graph for visualization. This project is still under development, 
so additions will be made when I have time. I am currently attending college so time 
to work on this is limited. 

To have an overview of the database, launch your browser at localhost:8080, and you will 
be able to login to the database at the IPV4 listed in 
```bash 
docker network inspect bridge
``` 
for the sqldata container.


[Back to top](#dockercryptoservice)
