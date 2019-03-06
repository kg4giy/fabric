from fabric.api import env
from fabric.operations import run, put

env.hosts = [
    'pi@192.168.1.181',
    'pi@192.168.1.183',
    'pi@192.168.1.184'
]

env.password = 'password'

def copy():
	# Make sure the directory is there
	run('mkdir -p /home/pi/.ssh')

	#our local directory to copy
	put('/home/pi/.ssh/authorized_keys', '/home/pi/.ssh')
