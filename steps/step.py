import time

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
    Utils.execute_command(Repo.uptime_command)
    result = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
    print("\nResult = {}".format(result))
    print("\nRebooting the {} host...".format(Conf.HOST))
    Utils.execute_reboot_command(Repo.reboot_command)
    Repo.client.close()
    print("Action after sent reboot command")

@When("check")
def step_impl(context):
    time.sleep(30)
    if Utils.connect():
        print("Again connected to the {} host".format(Conf.HOST))




        # status = True
        # count = 0
        # while (status):
        #     if count > 0:
        #         if (Utils.connect()):
        #             status = False
        #             print("---connected---")
        #         else:
        #             if count > 10:
        #                 print("The remote host {} is not reachable!".format(Conf.HOST))
        #             else:
        #                 print("---not connected---")
        #                 time.sleep(3)
        #                 count += 1


        # Utils.execute_command(Repo.check_command)
        # result = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
        # print("\nResult = {}".format(result))

        # count = 0
        # while (result > 60.00):
        #     time.sleep(3)
        #     if (Utils.connect()):
        #         if count > 10:
        #             print("The remote host {} is not reachable!".format(Conf.HOST))
        #         else:
        #             Utils.execute_command(Repo.uptime_command)
        #             result = Repo.ssh_output.decode("utf-8").rstrip("\n\r")
        #             count += 1
        #             print("\Count = {}".format(count))
        #
        #
        # Repo.result = result
        # print("\nResult = {}".format(result))


# @Then("the result should be (.*)")
# def step_impl(context, expected_result):
#     actual_result = repo.result
#     assert expected_result in actual_result, "\nactual_result:\n{}\nexpected_result\n{}".format(actual_result,
#                                                                                                 expected_result)
#
#
# @Then("the command status should be (.*)")
# def step_impl(context, expected_command_status):
#     actual_command_status = repo.status
#     assert actual_command_status == expected_command_status, \
#         "\nactual_command_status:\n{}\nexpected_command_status\n{}".format(actual_command_status,
#                                                                            expected_command_status)
#
#
# @Then("the last time reboot of system should be less than (.*) seconds")
# def step_impl(context, expected_timeout):
#     ssh.execute_command(repo.uptime_command)
#     actual_timeout = repo.ssh_output.decode("utf-8").rstrip("\n\r")
#     assert actual_timeout < expected_timeout, "\nactual_timeout:\n{}\nexpected_timeout\n{}".format(actual_timeout,
#                                                                                                    expected_timeout)


# @Given("start")
# def step_impl(context):
#     print("\nStart...")
#
# @When("todo")
# def step_impl(context):
#     # ssh.execute_command('ls -l')
#     # result = repo.ssh_output.decode("utf-8")
#     # print("\nResult is: {}".format(result))
#     print("\nWhen...")
#
# @Then("finish")
# def step_impl(context):
#     print("\n...Finish")



@Given("the check command is provided")
def step_impl(context):
    Repo.check_command = context.text
