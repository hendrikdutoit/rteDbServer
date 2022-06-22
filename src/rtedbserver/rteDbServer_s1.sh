#!/bin/bash
clear

# Variables
_sytem=$1 # Ini configuration file specific to platform and machine
_usr_dir=/usr
_venv_dir=$_usr_dir/venv
_rte_install_venv=$_venv_dir/rte_dev_db_env
_rte_install_dir=$_rte_install_venv/lib/python3.10/site-packages/rtedbserver

# Create instlation sudo user
user_name='rtinstall'
#useradd $user_name
adduser $user_name
usermod -aG sudo $user_name

# Install pre-req packages
apt update
apt-get -y install python3-pip
apt-get -y install mysql-server
apt-get -y install python3-venv

# Install home-grown packages
mkdir $_venv_dir
chmod 777 $_venv_dir
python3 -m venv --clear $_rte_install_venv
source $_rte_install_venv/bin/activate
pip install --upgrade InstallIt
pip install --upgrade git+https://github.com/hendrikdutoit/rteDbServer.git

#Install and configure the server packages
cp /usr/local/share/rteDbServer_s1_$_system.ini $_rte_install_dir/rteDbServer_s1.ini
python3 $_rte_install_dir/rtedbserver.py -c $_rte_install_dir/rteDbServer_s1.ini


# Prompt to close the session
echo Session completed
echo Press any key to finsh and quit
#read quit
