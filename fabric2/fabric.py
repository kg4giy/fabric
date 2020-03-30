from fabric import Connection

for host in ('192.168.1.181', '192.168.1.183', '192.168.1.184' '192.168.1.231')
	result = Connection(host).run('uname -s')
	print("{}: {}".format(host, result.stdout.strip()))