@ECHO ON
@REM "C:\Program Files\Beyond Compare 4\BCompare.exe" @"InstallServer.txt" 178.62.45.198 138.68.152.245
ssh -t -E D:\Dropbox\Projects\RealTimeEvents\install\rteInstallRTEServer_s1.log root@178.62.45.198 "bash -x //usr/local/share/rteInstallRTEServer_s1.sh"
ssh -t -E rteInstallRTEServer_s2.log rtinstall@178.62.45.198 "bash -x //usr/local/share/rteInstallRTEServer_s2.sh rteInstallRTEServer_s2.ini"
@REM CALL UpdateWebServer_01_dev02.bat
