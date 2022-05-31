@ECHO ON
ssh -t -E D:\Dropbox\Projects\rteDbServer\src\rteDbServer\rteDbServer.log root@159.65.19.237 "ufw enable;ufw allow OpenSSH;apt update;apt install openssh-server;ufw allow 22;systemctl start ssh"
REM scp d:\Dropbox\Projects\rteDbServer\src\rteDbServer\rteDbServer_s1.* root@159.65.19.237://usr/local/share
REM scp d:\Dropbox\Projects\rteDbServer\data\.netrc root@159.65.19.237:~/.netrc
REM ssh -t -E D:\Dropbox\Projects\rteDbServer\src\rteDbServer\rteDbServer.log root@159.65.19.237 "cd /usr/local/share;sudo chmod 777 rteDbServer_s1.sh;bash -x /usr/local/share/rteDbServer_s1.sh rteDbServer_s1.ini"
@REM CALL UpdateWebServer_01_dev02.bat
