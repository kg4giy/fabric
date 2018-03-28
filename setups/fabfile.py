from fabric.api import *
from fabric.operations import run, put

env.hosts = [
    'pi@192.168.20.101',
    'pi@192.168.20.103',
    'pi@192.168.20.106'
]

# Alternate for AWS
# env.hosts=["user@instance-region.compute.amazonaws.com"]

env.key_filename = '/home/pi/.ssh/pi.pem'
# Alternate
# env.key_filename=['/home/pi/.ssh/pi.pem']
# env.password = 'password'

# Reference https://stackoverflow.com/questions/5327465/using-an-ssh-keyfile-with-fabric/28409635

@parallel
def cmd(command):
    sudo(command)


def copy():
	# Make sure the directory is there
	run('mkdir -p /home/pi/.ssh')

	#our local directory to copy
	put('/home/pi/.ssh/authorized_keys', '/home/pi/.ssh')
