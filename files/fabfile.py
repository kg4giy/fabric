from fabric.api import env
from fabric.operations import run, put

env.hosts = [
    'pi@192.168.20.101',
    'pi@192.168.20.103',
    'pi@192.168.20.106'
]

env.password = 'password'

def copy():
	# Make sure the directory is there
	run('mkdir -p /home/pi/.ssh')

	#our local directory to copy
	put('/home/pi/.ssh/authorized_keys', '/home/pi/.ssh')