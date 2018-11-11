Feature: ssh

  Discription: Perform a connection to remote machine via ssh


  Scenario: Connection

    Given the remote host 79.143.35.147 is provided

    When the command is performed
    """
    cp /dev/null tmp.log
    pwd >> tmp.log
    date >> tmp.log
    ls -alh >> tmp.log
    """

    Then the ssh connection is Ok