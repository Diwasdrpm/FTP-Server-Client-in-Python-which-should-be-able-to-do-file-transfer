import ftplib
ftphost_server = 'localhost'
ftpPortNo = 21
ftpusername= 'abcd'
ftpPass = '852456'
ftp_instance = ftplib.FTP()
ftp_instance.connect(ftphost_server,ftpPortNo)
ftp_instance.login(ftpusername,ftpPass)
ftp_instance.cwd("folder1/")

targetfilename = "Compiler Design.pdf"
localfilepath = targetfilename

with open(localfilepath,'wb') as file:
    file_download = ftp_instance.retrbinary(f"RETR {targetfilename}",file.write)

ftp_instance.quit()

if file_download.startswith("226"):
    print("download success!")
else:
    print("download not success")