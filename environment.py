from Repo import Repo
from behave.log_capture import capture


def before_all(context):
    context.config.setup_logging()


@capture
def before_scenario(context, scenario):
    Repo.result = None
    Repo.reboot_command = None
    Repo.uptime_command = None
    Repo.client = None
    Repo.ssh_output = None
    Repo.ssh_error = None


@capture
def after_scenario(context, scenario):
    Repo.client.close()
    print("\nThe SSH connection is closed.")
