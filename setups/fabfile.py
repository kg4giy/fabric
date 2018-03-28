from fabric.api import *

env.hosts = [
    'pi@192.168.20.101',
    'pi@192.168.20.103',
    'pi@192.168.20.106'
]

env.password = 'password'

@parallel
def cmd(command):
    sudo(command)
