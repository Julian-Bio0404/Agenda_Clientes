"""Logica"""

import csv
import os
from clients.models import Client

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        #modo append
        with open(self.table_name, mode="a") as f:
            #definir columnas segun el modelo
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            #convertir a dict el cliente que recibimos
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode="r") as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_client):
        clients = self.list_clients()
        
        updated_clients = []
        for client in clients:
            if client["uid"] == updated_client.uid:
                updated_clients.append(updated_client.to_dict()) #to_dict para que python escriba como diccionario al csv
            else:
                updated_clients.append(client)
        
        self._save_to_disk(updated_clients)

    def delete_client(self, row_uid):
        rows = self.list_clients()
        updated_rows = [row for row in rows if row['uid'] != row_uid]

        self._save_to_disk(updated_rows)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + ".tmp"
        with open(tmp_table_name, mode="w") as f:
            writer = csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerows(clients)
        
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)


