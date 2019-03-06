#!/usr/bin/env python
from fabric.api import run, sudo, task, get, put, env

env.hosts = [
    'pi@192.168.1.181',
    'pi@192.168.1.183',
    'pi@192.168.1.184'
]

env.key_filename = "~/.ssh/pi.pem"
env.password = 'password'

def copy():
        # Make sure the directory is there
        run('mkdir -p /home/pi/.ssh')

        #our local directory to copy
        put('/home/pi/.ssh/authorized_keys', '/home/pi/.ssh')

@task
def cmdrun(arg):
	run(arg)

@task
def sudorun(arg):
	sudo(arg)

@task
def download(arg):
	get(remote_path=arg, local_path="/tmp/", use_sudo=True)

@task
def upload(arg1, arg2):
	put(local_path=arg1, remote_path=arg2, use_sudo=True)

