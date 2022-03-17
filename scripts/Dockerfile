FROM ubuntu:latest

#Set working directory in container and copy all contents there
WORKDIR /usr/src/app
COPY . .

ENV TZ=US/Eastern
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#Run apt commands
RUN apt update 
#Maybe don't need packages
RUN apt install syslog-ng iputils-ping vim net-tools -yq --no-install-recommends
#Definitely need packages
RUN DEBIAN_FRONTEND=noninteractive apt install ca-certificates postfix mailutils python3 apt-utils nmap make libmgl-dev libmariadb-dev mariadb-client libjson-c-dev libcurl4-openssl-dev libmgl-dev curl g++ bash -yq --no-install-recommends && rm -rf /var/lib/apt/lists/*

#Make the project with current libraries
RUN make

#Run post DB-runnning script
RUN chmod +x script.sh
CMD ./script.sh
