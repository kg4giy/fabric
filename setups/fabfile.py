from fabric.api import *

env.hosts = [

    'pi@',
    'pi@',
    'pi@',
]

env.password = 'raspberry'

@parallel
def cmd(command):
    sudo(command)
