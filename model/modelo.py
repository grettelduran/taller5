import json

class Player:
    def __init__(self, username, password, name, last_name, email, avatar):
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.email = email
        self.avatar = avatar

    def to_JSON_string(self):
        #esto permite convertir el objeto en json string
        cad = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)
        print(cad)
        return cad