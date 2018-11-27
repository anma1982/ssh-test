# POC

This is Gherkin scenario which uses Python language with Behave framework.<br> 
The program reboots a remote machine and checks actions result.

"features.ssh.feature" contains Gherkin scenario<br>
"steps.Step.py" contains a Gherkin scenario implementation<br>
"Conf.py" contains constant values<br>
"environment.py" contains a hook which is performed after each scenario<br>
"Repo.py" contains variables<br>
"setup.cfg" contains Behave command-line arguments<br>
"Utils.py" contains subsidiary methods

For running scenario from command line:<br>
behave -o reports/report.log<br>
behave -f json -o reports/report.json