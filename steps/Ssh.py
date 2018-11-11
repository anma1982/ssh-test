from behave import *
from utils.SshUtil import SshUtil

use_step_matcher("re")


@Given("the remote host (.*) is provided")
def step_impl(context, IPAddress):
    print("\nThe remote host is: {}".format(IPAddress))

@When('the command is performed')
def step_impl(context):
    command = context.text
    ssh_obj = SshUtil()
    ssh_obj.execute_command(command)
    print("\nThe {} command is performed".format(command))

@Then("the ssh connection is (.*)")
def step_impl(context, connectionStatus):
    print("\nThe connection status is: {}".format(connectionStatus))