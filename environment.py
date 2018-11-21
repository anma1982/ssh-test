from Repo import Repo


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    Repo.client.close()
    print("\nThe SSH connection is closed.")
