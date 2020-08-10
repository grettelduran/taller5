from database.base_datos import BaseDatos
from model.modelo import Player
from os import system, name


class Controller:
    def __init__(self):
        self.bd = BaseDatos()
        self.inicio()

    def inicio(self):
        print("Api Player:")

    def add_new_player(self, username, password, name, last_name, email, avatar):
        player = Player(username, password, name, last_name, email, avatar)
        return self.bd.add_new_player(player)
        
    def get_all_players(self):
        return self.bd.get_all_players()

    def login(self, username, password):
        return self.bd.login(username, password)
