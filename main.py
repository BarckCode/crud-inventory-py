import sys

clients = [
	{
		'name': 'Pablo',
		'company': 'Google',
		'email': 'pablo@google.com',
		'position': 'Frontend Engineer',
	},
	{
		'name': 'Ricardo',
		'company': 'Google',
		'email': 'ricardo@google.com',
		'position': 'Backend Engineer',
	},
]

# Welcome Message
def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[R]ead clients list')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


# Utils
def _get_client_field(field):
	client = input(f'What is the client {field}? ')

	return client


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


# Actions
def create_client(client_name):
	global clients

	if client_name not in clients:
		clients.append(client_name)
	else:
		print('Client already is in the clients list')


def list_clients():
	for uid, client in enumerate(clients):
		name = client['name']
		company = client['company']
		email = client['email']
		position = client['position']

		print(f'{uid} | {name} | {company} | {email} | {position}')


def update_client(client_id, updated_client):
	global clients

	if len(clients) - 1 >= client_id:
		clients[client_id] = updated_client
	else:
		print(f'{client_id} is not in clients list')


def delete_client(client_id):
	global clients

	for uid, client in enumerate(clients):
		if uid == client_id:
			del clients[uid]
			break

def search_client(client_name):
	for client in clients:
		if client['name'] != client_name:
			continue
		else:
			return True


# Entry Program
if __name__ == '__main__':
	_print_welcome()

	command = input('Select option: ')
	command = command.upper()

	if command == 'C':
		client = _get_client_from_user()
		create_client(client)
		list_clients()
	elif command == 'R':
		list_clients()
	elif command == 'U':
		print('What item do you want to edit?')
		print('Select an id:')
		list_clients()
		client_id = int(_get_client_field('id'))
		updated_client = _get_client_from_user()

		update_client(client_id, updated_client)
		list_clients()
	elif command == 'D':
		print('What item do you want to delete?')
		print('Select an id:')
		list_clients()
		client_id = int(_get_client_field('id'))

		delete_client(client_id)
		list_clients()
	elif command == 'S':
		client_name = _get_client_field('name')
		found = search_client(client_name)

		if found:
			print(f'{client_name} is in the clients list')
		else:
			print(f'The client {client_name} is not in our clients list')
	else:
		print('Invalid option')