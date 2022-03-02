import ftplib
ftphost_server = 'localhost'
ftpPortNo = 21
ftpusername= 'abcd'
ftpPassword = '852456'
ftp_instance = ftplib.FTP()
ftp_instance.connect(ftphost_server,ftpPortNo)
ftp_instance.login(ftpusername,ftpPassword)
ftp_instance.cwd("folder1/")
localfilepath = "D:/Major_Project/task2.log"

with open(localfilepath , 'rb') as file:
    file_upload = ftp_instance.storbinary("STOR task2.log",file)

ftp_instance.quit()

if file_upload.startswith("226"):
    print("upload successfull")
else:
    print("upload not successfull")

print("This task is Successfully Completed")