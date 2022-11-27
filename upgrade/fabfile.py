from fabric import Connection, run, sudo, task, get, put, env

env.hosts = [
	'pi@192.168.1.240',
	'pi@192.168.1.181',
	'pi@192.168.1.183',
	'pi@192.168.1.184',
	'pi@192.168.1.75',
	'pi@192.168.1.173',
	'pi@192.168.1.231',
	'pi@192.168.1.243',
	'pi@192.168.1.232',
	'pi@192.168.1.238',
	'pi@192.168.1.243',
	'pi@192.168.1.248',
	'pi@192.168.1.199',
	'pi@192.168.1.244',
	'pi@192.168.1.241',
]

env.key_filename = '/home/pi/.ssh/pi.pem'

@parallel 
def cmd[command]:
	sudo[command]