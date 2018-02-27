import os
from elections.storage.connection import Connection

FILE_NAME = 'users.txt'

class Accounts:

    def __init__(self):
        self.accounts = Connection.read_from_file(FILE_NAME)

    def check_user(self, user):
        return user in self.accounts