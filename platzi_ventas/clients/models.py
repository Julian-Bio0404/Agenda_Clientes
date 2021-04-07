"""Modelo"""

import uuid #permite generar uids unicas

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        #checa lo que el metodo dict regresa y permite acceder a 
        # una representacion de diccionario de nuestro objeto client
        # para poder guardarlo en disco
        return vars(self) 

    #permite declarar metodos estaticos
    @staticmethod
    def schema():
        return["name", "company", "email", "position", "uid"]