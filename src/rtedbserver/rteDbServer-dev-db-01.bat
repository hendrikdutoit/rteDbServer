@ECHO ON
if "%1"=="" (
    set /P _system="System (Dev/Prod): "
    ) else (
    set _system=%1
)
set _app_root_dir="d:\Dropbox\Projects\rteDbServer"

copy %_app_root_dir%\src\rteDbServer\rte_DbServer_UT_s1.ini %_app_root_dir%\src\rteDbServer\rteDbServer_s1.ini
ssh -t -E %_app_root_dir%\rteDbServer\src\rteDbServer\rteDbServer.log root@159.65.212.97 "ufw enable;ufw allow OpenSSH;apt update;apt install openssh-server;ufw allow 22;systemctl start ssh"
scp %_app_root_dir%\rteDbServer\src\rteDbServer\rteDbServer_s1*.* root@159.65.212.97://usr/local/share
scp %_app_root_dir%\rteDbServer\data\.netrc root@159.65.212.97:~/.netrc
ssh -t -E %_app_root_dir%\src\rteDbServer\rteDbServer.log root@159.65.212.97 "cd /usr/local/share;sudo chmod 777 rteDbServer_s1.sh;bash -x /usr/local/share/rteDbServer_s1.sh %_system%"
@REM CALL UpdateWebServer_01_dev02.bat
