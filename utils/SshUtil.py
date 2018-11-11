import paramiko
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import SshConf as conf_file
import socket


class SshUtil:
    "Class to connect to remote server"

    def __init__(self):
        self.ssh_output = None
        self.ssh_error = None
        self.client = None
        self.host = conf_file.HOST
        self.username = conf_file.USERNAME
        self.password = conf_file.PASSWORD
        self.timeout = float(conf_file.TIMEOUT)
        self.commands = conf_file.COMMANDS
        self.pkey = conf_file.PKEY
        self.port = conf_file.PORT
        self.uploadremotefilepath = conf_file.UPLOADREMOTEFILEPATH
        self.uploadlocalfilepath = conf_file.UPLOADLOCALFILEPATH
        self.downloadremotefilepath = conf_file.DOWNLOADREMOTEFILEPATH
        self.downloadlocalfilepath = conf_file.DOWNLOADLOCALFILEPATH

    def connect(self):
        "Login to the remote server"
        try:
            # Paramiko.SSHClient can be used to make connections to the remote server and transfer files
            print("\nEstablishing ssh connection...")
            self.client = paramiko.SSHClient()
            # Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the server
            if (self.password == ''):
                self.pkey = paramiko.RSAKey.from_private_key_file(self.pkey)
                self.client.connect(hostname=self.host, port=self.port, username=self.username, pkey=self.pkey,
                                    timeout=self.timeout, allow_agent=False, look_for_keys=False)
                print("\nConnected to the server:\n{}".format(self.host))
            else:
                self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password,
                                    timeout=self.timeout, allow_agent=False, look_for_keys=False)
                print("\nConnected to the server:\n{}".format(self.host))
        except paramiko.AuthenticationException:
            print("\nAuthentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("\nCould not establish SSH connection: %s" % sshException)
            result_flag = False
        except socket.timeout as e:
            print("\nConnection timed out")
            result_flag = False
        except Exception as e:
            print('\nException in connecting to the server')
            print('PYTHON SAYS:', e)
            result_flag = False
            self.client.close()
        else:
            result_flag = True
        return result_flag

    def execute_command(self, command):
        """Execute a command on the remote host.Return a tuple containing
        an integer status and a two strings, the first containing stdout
        and the second containing stderr from the command."""
        self.ssh_output = None
        result_flag = True
        try:
            if self.connect():
                # for command in commands:
                print("\nExecuting command:\n{}".format(command))
                stdin, stdout, stderr = self.client.exec_command(command, self.timeout)
                self.ssh_output = stdout.read()
                self.ssh_error = stderr.read()
                if self.ssh_error:
                    print("\nProblem occurred while running command:\n{}".format(command))
                    print("\nThe error is: \n{}".format(self.ssh_error))
                    result_flag = False
                else:
                    print("\nCommand execution completed successfully:\n{}".format(command))
                self.client.close()
            else:
                print("\nCould not establish SSH connection")
                result_flag = False
        except socket.timeout as e:
            print("\nCommand timed out\n{}\n{}".format(self.client.close(), result_flag=False))
        except paramiko.SSHException:
            print("\nFailed to execute the command:\n{}\n{}".format(command, self.client.close()))
            result_flag = False
        return result_flag

    def upload_file(self, uploadlocalfilepath, uploadremotefilepath):
        "This method uploads the file to remote server"
        result_flag = True
        try:
            if self.connect():
                ftp_client = self.client.open_sftp()
                ftp_client.put(uploadlocalfilepath, uploadremotefilepath)
                ftp_client.close()
                self.client.close()
            else:
                print("Could not establish SSH connection")
                result_flag = False
        except Exception as e:
            print("\nUnable to upload the file to the remote server:\n{}".format(uploadremotefilepath))
            print("\nPYTHON SAYS:", e)
            result_flag = False
            ftp_client.close()
            self.client.close()
        return result_flag

    def download_file(self, downloadremotefilepath, downloadlocalfilepath):
        "This method downloads the file from remote server"
        result_flag = True
        try:
            if self.connect():
                ftp_client = self.client.open_sftp()
                ftp_client.get(downloadremotefilepath, downloadlocalfilepath)
                ftp_client.close()
                self.client.close()
            else:
                print("Could not establish SSH connection")
                result_flag = False
        except Exception as e:
            print("\nUnable to download the file from the remote server:\n{}".format(downloadremotefilepath))
            print("\nPYTHON SAYS:", e)
            result_flag = False
            ftp_client.close()
            self.client.close()
        return result_flag
