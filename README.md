# pmkid auto wifi cracking tool
# Simple script that can be modify by user to work for them,
# Please feel free to send me comments on twitter
# All install requirement are already in script, But will also add to repo

#Install and update below package first before install tools 
1: apt-get update
2: apt-get dist-upgrade -y
3: apt-get install libssl-dev
4: apt-get install libz-dev
5: apt-get install libpcap-dev
6: apt-get install libcurl4-openssl-dev

# Download and install below tools
# make 
#make install
git clone https://github.com/hashcat/hashcat.git
git clone https://github.com/ZerBea/hcxdumptool.git
git clone https://github.com/ZerBea/hcxtools.git

