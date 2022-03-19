import json
import os
import time
import re
import subprocess

def openPorts(port):
    output = subprocess.check_output(f"nmap -n -p {port} 172.17.0.0/24", shell=True).decode()

    split = [i for i in output.split("\n") if len(i) > 1]
    ips = []
    status = []
    for i in split:
        x = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", i)
        if x:
            ips.append(x[0])
        y1 = re.findall("open", i)
        y2 = re.findall("closed", i)
        if y1:
            status.append(y1[0])
        if y2:
            status.append(y2[0])

    ips = ips[1:]
    status = status[1:]

    for i,v in enumerate(ips):
        if(status[i] == "open"):
            return v

    return None


def change_project_json(ip):
    #Opens json file for reading 
    with open("project.json", "r") as j:
        obj = json.load(j)
        obj["Hostname"] = ip

        code = os.system(f'mysql -u{obj["Username"]} -p{obj["Password"]} -h{ip} {obj["Database"]} < crypto.sql')
        print(f'mysql command executed with code {code}')

    #Opens json file for writing updated file
    with open("project.json", "w") as j:
        json.dump(obj, j, indent="\t")


def change_postfix_conf(ip):
    os.system(f'postconf -e "myhostname"="{os.environ["HOSTNAME"]}"')
    os.system(f'postconf -e "relayhost"="{ip}"')
    os.system(f'postconf -e "inet_interfaces"="loopback-only"')
    os.system(f'postconf -e "local_transport"="error: local delivery disabled"')
    os.system(f'postconf -e "mydestination"=""')
    os.system('rm -f /var/spool/postfix/pid/master.pid')
    os.system('exec /usr/sbin/postfix start')




if __name__ == "__main__":

    time.sleep(30)
    mariadb_ip = openPorts(3306)
    postfix_ip = openPorts(25)

    change_project_json(mariadb_ip)
    #change_postfix_conf(postfix_ip)



