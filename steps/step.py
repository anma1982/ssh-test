import os
import time
from subprocess import Popen, PIPE

from behave import *

from Repo import Repo
from Utils import Utils
import Conf

use_step_matcher("re")


@Given("the uptime command is provided")
def step_impl(context):
    Repo.uptime_command = context.text


@Given("the ssh connection is established")
def step_impl(context):
    Utils.connect()


@Given("the reboot command is provided")
def step_impl(context):
    Repo.reboot_command = context.text


@Given("the test command is provided")
def step_impl(context):
    Repo.command = context.text


@When("the reboot command is processed")
def step_impl(context):
    print("\nRebooting the {} host...".format(Conf.HOST))
    Repo.client.close()
    os.system(Repo.reboot_command)
    count = 0
    status = True
    while (status):
        if (Utils.connect()):
            Utils.execute_command(Repo.uptime_command)
            Repo.result = float(Repo.ssh_output.decode("utf-8").rstrip("\n\r"))
            if Repo.result > 60.00:
                Utils.execute_command(Repo.uptime_command)
                Repo.result = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
                time.sleep(3)
                continue
            else:
                status = False
                print("\n======================= The host {} connected again :) =======================".format(
                    Conf.HOST))
                Utils.execute_command(Repo.uptime_command)
                Repo.result = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
        else:
            if count > 30:
                print("The remote host {} is not reachable :(".format(Conf.HOST))
                break
            else:
                print("Still not connected...")
                time.sleep(3)
                count += 1


@Then("the last time reboot of system should be less than (.*) seconds")
def step_impl(context, expected_timeout):
    Utils.execute_command(Repo.uptime_command)
    actual_timeout = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
    print("\nActual timeout: {}\nExpected timeout: {}".format(actual_timeout, expected_timeout))
    assert actual_timeout < expected_timeout, "\nActual timeout: {}\nExpected timeout: {}".format(actual_timeout,
                                                                                                  expected_timeout)
