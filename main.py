from models.admin import Admin
from models.node import Node

class Marzban:
    def __init__(self, username: str, password: str, address: str) -> None:
        self.username = username
        self.password = password
        self.address = address
        self.admin = Admin(username, password, address) 
        self.node = Node(username, password, address)
