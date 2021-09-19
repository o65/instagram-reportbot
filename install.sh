if [[ $EUID -ne 0 ]]; then
   echo "[-] Please run as root" 
   exit 1
fi
clear
echo "Installing requirements"

pip3 install requests
pip3 install colorama
pip3 install getpass