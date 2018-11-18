Feature: ssh

  Discription: Perform a connection to remote machine via ssh

  Background:

    Given the uptime command is provided
    """
    awk '{print $1}' /proc/uptime
    """
    And the check command is provided
    """
    echo $?
    """
    And the ssh connection is established


  Scenario: Reboot remote machine

    Given the reboot command is provided
    """
    (sleep 5; reboot) &
    """

    When the reboot command is processed
    And check

#    Then the command status should be 0
#    And the last time reboot of system should be less than 60 seconds

#    Given start
#
#    When todo
#
#    Then finish