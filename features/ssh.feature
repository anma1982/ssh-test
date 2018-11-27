Feature: POC

  Description: Perform a connection to remote machine via ssh

  Background:

    Given the uptime command is provided
    """
    awk '{print $1}' /proc/uptime
    """
    And the ssh connection is established


  Scenario: Remote host rebooting

    Given the reboot command is provided
    """
    (sshpass -p 'iddqd' ssh root@10.0.0.114 'reboot') &
    """

    When the reboot command is processed

    Then the last time reboot of system should be less than 60 seconds
