import json
from model.modelo import Player
from os import system, name
import re 
  
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class BaseDatos:
    def load_existing_players(self):
        with open('existing_users.json') as json_file:
            data = json.load(json_file)
            existing_players = []
            for value in data:
                player = Player(
                value.get("username"),
                value.get("password"),
                value.get("name"),
                value.get("last_name"),
                value.get("email"),
                value.get("avatar"))
                existing_players.append(player)
            return existing_players
    def pass_validations(self, objPlayer):
        for player in self.existing_players:
            if player.username == objPlayer.username or player.email == objPlayer.email:
                print("User or Email already exists")
                return False
        if re.search(email_regex,objPlayer.email):  
            if re.search(r"\s", objPlayer.username):
                print("username shouldn't have spaces")
                #TODO missing validation for password
                return False
            else:
                return True
        else:
            print("Invalid email")
            return False  
    def add_new_player(self, objPlayer):
        if self.pass_validations(objPlayer):
            self.existing_players.append(objPlayer)
            playersJson = []
            for player in self.existing_players:
                playersJson.append(player.to_JSON_string())
            separator =","
            result = "["+separator.join(playersJson)+"]"
            print(result)
            with open("existing_users.json", "w") as outfile:
                outfile.write(result)
            return "New player added successfuly"
        else:
            return "Player couldn't be added"
    def __init__(self):
        self.existing_players = self.load_existing_players()

    def get_all_players(self):
        return self.existing_players
    def get_player_by_username(self, username):
        for player in self.existing_players:
            if player.username == username:
                return player
        return None
    def login(self, username, password):
        tempPlayer = self.get_player_by_username(username)
        if tempPlayer != None:
            if tempPlayer.password == password:
                return "Correct credentials"
            else:
                return "Wrong password"    
        else:
            return "User doesn't exists"
