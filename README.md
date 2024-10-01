### Install dependencies in current folder

To install all the python dependencies in the current folder execute the file LinuxInstallDependencies.sh or MacInstallDependencies.sh

`$ bash LinuxInstallDependencies.sh`

`$ bash MacInstallDependencies.sh`

If you encounter the error ModuleNotFoundError or command not found, run the command

`$ source env/bin/activate`

### Add IBM token 

To add your ibm token execute tokenSetup.sh passing your token as argument

`$ bash tokenSetup.sh <your_ibm_token>`
