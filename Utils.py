import paramiko
import os, sys

from Repo import Repo

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Conf
import socket

class Utils:

    @staticmethod
    def connect():
        try:
            print("\nEstablishing ssh connection...")
            Repo.client = paramiko.SSHClient()
            Repo.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if (Conf.PASSWORD == ''):
                Conf.PKEY = paramiko.RSAKey.from_private_key_file(Conf.PKEY)
                Repo.client.connect(hostname=Conf.HOST, port=Conf.PORT, username=Conf.USERNAME, pkey=Conf.PKEY,
                                    timeout=Conf.TIMEOUT, allow_agent=False, look_for_keys=False)
                print("\nConnected to the server:\n{}:{}".format(Conf.HOST, Conf.PORT))
            else:
                Repo.client.connect(hostname=Conf.HOST, port=Conf.PORT, username=Conf.USERNAME, password=Conf.PASSWORD,
                                    timeout=Conf.TIMEOUT, allow_agent=False, look_for_keys=False)
                print("\nConnected to the server:\n{}:{}".format(Conf.HOST, Conf.PORT))
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
            Repo().client.close()
        else:
            result_flag = True
        return result_flag

    def execute_command(command):
        Repo.ssh_output = None
        result_flag = True
        try:
            print("\nExecuting command:\n{}".format(command))
            stdin, stdout, stderr = Repo.client.exec_command(command, Conf.TIMEOUT)
            Repo.ssh_output = stdout.read()
            Repo.ssh_error = stderr.read()
            if Repo.ssh_error:
                print("\nProblem occurred while running command:\n{}".format(command))
                print("\nThe error is: \n{}".format(Repo.ssh_error))
                result_flag = False
            else:
                print("\nCommand execution completed successfully:\n{}".format(command))
                # Repo.client.close()
        except socket.timeout as e:
            print("\nCommand timed out\n{}".format(Repo.client.close(), result_flag=False))
        except paramiko.SSHException:
            print("\nFailed to execute the command:\n{}\n{}".format(command, Repo.client.close()))
            result_flag = False
        return result_flag

    def execute_reboot_command(command):
        Repo.ssh_output = None
        result_flag = True
        try:
            print("\nExecuting command:\n{}".format(command))
            stdin, stdout, stderr = Repo.client.exec_command(command, Conf.TIMEOUT)
            Repo.ssh_output = stdout.read()
            Repo.ssh_error = stderr.read()
            if Repo.ssh_error:
                print("\nProblem occurred while running command:\n{}".format(command))
                print("\nThe error is: \n{}".format(Repo.ssh_error))
                result_flag = False
            else:
                print("\nCommand execution completed successfully:\n{}".format(command))
                Repo.client.close()
        except socket.timeout as e:
            print("\nCommand timed out\n{}".format(Repo.client.close(), result_flag=False))
        except paramiko.SSHException:
            print("\nFailed to execute the command:\n{}\n{}".format(command, Repo.client.close()))
            result_flag = False
        return result_flag

    # def upload_file(self, uploadlocalfilepath, uploadremotefilepath):
    #     result_flag = True
    #     try:
    #         if self.connect:
    #             ftp_client = Repo().client.open_sftp()
    #             ftp_client.put(uploadlocalfilepath, uploadremotefilepath)
    #             ftp_client.close()
    #             # repo.client.close()
    #         else:
    #             print("Could not establish SSH connection")
    #             result_flag = False
    #     except Exception as e:
    #         print("\nUnable to upload the file to the remote server:\n{}".format(uploadremotefilepath))
    #         print("\nPYTHON SAYS:", e)
    #         result_flag = False
    #         ftp_client.close()
    #         # repo.client.close()
    #     return result_flag
    #
    # def download_file(self, downloadremotefilepath, downloadlocalfilepath):
    #     result_flag = True
    #     try:
    #         if self.connect:
    #             ftp_client = Repo().client.open_sftp()
    #             ftp_client.get(downloadremotefilepath, downloadlocalfilepath)
    #             ftp_client.close()
    #             # repo.client.close()
    #         else:
    #             print("Could not establish SSH connection")
    #             result_flag = False
    #     except Exception as e:
    #         print("\nUnable to download the file from the remote server:\n{}".format(downloadremotefilepath))
    #         print("\nPYTHON SAYS:", e)
    #         result_flag = False
    #         ftp_client.close()
    #         # repo.client.close()
    #     return result_flag
