import sys
import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []

def _initalize_clients_from_storage():
    with open(CLIENT_TABLE, mode="r") as f:
        #fieldnames es una lista de llaves que usa DictReader 
        #para construir los diccionarios
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


#Crea tabla temporal, la guarda en archivo CLIENT_TABLE
#y borra la tabla anterior
def _save_clients_to_storage():
    tmp_table_name = "{}.tmp".format(CLIENT_TABLE)
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


#Funcion que añade un nuevo client al diccionario clients
def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


#Imprime cada cliente con sus datos
def list_clients():
    print('uid|  name  | company  |  email   | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


#Funcion que recibe un diccionario con nuevos 
#datos y los actualiza segun el client_id
def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


#Funcion que elimina un client segun su client_id
def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


#Funcion que busca client por su nombre y devuelve 
#True si lo encuentra
def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


#Funcion que pregunta al usuario los campos, estos 
#serán entregados a _get_client_from _user()
def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))
    return field


#Funcion que arma un diccionario client, cuyos valores 
#son entregados por la funcion _get_client_field()
def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _initalize_clients_from_storage()
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

    else:
        print('Invalid command')

    _save_clients_to_storage()
