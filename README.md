PMKID
==========

Project can be download from: https://github.com/Zer1Ic3/pmkid
-----------------------------

Notes
-----
This script was from the view what i required, Please note that each user needs can change as they require

Authors
----------
Deon  
Twitter @zeroice28  

Required Package
-----------------
.:  
apt-get update  
apt-get dist-upgrade -y  
apt-get install libssl-dev  
apt-get install libz-dev  
apt-get install libpcap-dev  
apt-get install libcurl4-openssl-dev  

Required tools
---------------
git clone https://github.com/hashcat/hashcat.git (make && make install)  
git clone https://github.com/ZerBea/hcxdumptool.git(make && make install)  
git clone https://github.com/ZerBea/hcxtools.git(make && make install)  

Bash script
------------
#!/bin/bash  
cd /Pentesting/Wifi_tools/PMKID/bssid/  
sed 's/[^0-9,A-Z,]*//g' bssid.txt >> update_bssid.txt ((Line ref:32) wifi.py)  

Script Details
---------------
Check variables and make required change  
Check wordlst naming and edit if required  
