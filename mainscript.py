import subprocess
import requests

result = subprocess.check_output(["arp -v | grep -v 'Address\|Entries'"], shell=True)
raw_data = result.decode('utf-8')
r2=raw_data.split("\n")
trustedIP=[]

unauth="Unauthorised IP found on the network \n ----------------------- \n"
myIPlist = ['192.168.1.01', '192.168.1.3'] #list of trsuted IP addresses

for i in range(0,(len(r2)-1)):
        temp = str(r2[i]).split(' ')
        if temp[0] not in myIPlist:
                print(r2[i])
                requests.get('https://api.telegram.org/bot{INPUT_YOUR_BOT_TOKEN_HERE}/sendMessage?chat_id=370905990&text={0} {1} \n -----------------------'.format(unauth,r2[i]))