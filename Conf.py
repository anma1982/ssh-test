"""
This config file would have the credentials of remote server,
the commands to execute, upload and download file path details.
"""
#Server credential details needed for ssh
HOST='10.0.0.114'
USERNAME='root'
PASSWORD='iddqd'
PORT = 22
TIMEOUT = 10

#.pem file details
PKEY = '/home/amakarenko/Documents/Keys/id_rsa.pem'

#Sample file locations to upload and download
UPLOADREMOTEFILEPATH = '/etc/example/filename.txt'
UPLOADLOCALFILEPATH = 'home/filename.txt'
DOWNLOADREMOTEFILEPATH = '/etc/sample/data.txt'
DOWNLOADLOCALFILEPATH = 'home/data.txt'