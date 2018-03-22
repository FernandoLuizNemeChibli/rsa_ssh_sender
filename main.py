from paramiko import AutoAddPolicy
from paramiko import SSHClient
from sys import argv as arguments


def main(server,username,port,password,public_rsa_key):
	client=SSHClient()
	client.set_missing_host_key_policy(AutoAddPolicy())
	client.connect(server,username=username,port=port,password=password)
	client.exec_command('echo \"'+public_rsa_key+'\" >> ~/.ssh/authorized_keys')
	print 'Done!'

usage_example='\nUsage:\n    python '+arguments[0]+' <public_rsa_file> <server_adress> <user> [port] [server_password]'

public_rsa_key=None
try:
	with open(arguments[1],'r') as file:
		public_rsa_key=file.read()
except IndexError:
	print 'You must give a public RSA key file.'+usage_example
except IOError:
	print 'The public RSA key file does not exist.'+usage_example

if public_rsa_key:
	try:
		server=arguments[2]
	except IndexError:
		server=None
		print 'You must give the server adress.'+usage_example
	if server:
		try:
			user=arguments[3]
		except IndexError:
			user=None
			print 'You must give a user to access the server.'+usage_example
		if user:
			try:
				port=int(arguments[4])
			except:
				port=22
			try:
				password=arguments[5]
			except IndexError:
				password=None
			main(server,user,port,password,public_rsa_key)
