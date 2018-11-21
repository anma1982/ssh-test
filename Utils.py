import paramiko
import os
import sys

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
            result_flag = False
        except socket.timeout as e:
            print("\nConnection timed out")
            result_flag = False
        except Exception as e:
            result_flag = False
            Repo().client.close()
        else:
            result_flag = True
        return result_flag

    @staticmethod
    def execute_command(command):
        Repo.ssh_output = None
        result_flag = True
        try:
            stdin, stdout, stderr = Repo.client.exec_command(command, Conf.TIMEOUT)
            Repo.ssh_output = stdout.read()
            Repo.ssh_error = stderr.read()
            if Repo.ssh_error:
                print("\nProblem occurred while running command:\n{}".format(command))
                print("\nThe error is: \n{}".format(Repo.ssh_error))
                result_flag = False
        except socket.timeout as e:
            print("\nCommand timed out\n{}".format(Repo.client.close(), result_flag=False))
        except paramiko.SSHException:
            print("\nFailed to execute the command:\n{}\n{}".format(command, Repo.client.close()))
            result_flag = False
        return result_flag

    @staticmethod
    def execute_reboot_command(command):
        Repo.ssh_output = None
        result_flag = True
        try:
            stdin, stdout, stderr = Repo.client.exec_command(command, Conf.TIMEOUT)
            Repo.ssh_output = stdout.read()
            Repo.ssh_error = stderr.read()
            if Repo.ssh_error:
                print("\nProblem occurred while running command:\n{}".format(command))
                print("\nThe error is: \n{}".format(Repo.ssh_error))
                result_flag = False
            else:
                Repo.client.close()
        except socket.timeout as e:
            print("\nCommand timed out\n{}".format(Repo.client.close(), result_flag=False))
        except paramiko.SSHException:
            print("\nFailed to execute the command:\n{}\n{}".format(command, Repo.client.close()))
            result_flag = False
        return result_flag