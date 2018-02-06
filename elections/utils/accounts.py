import os

ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

class Accounts:

    def __init__(self):
        self.accounts = []
        self.user_file = open(ROOT('users.txt'), "r")
        for i, line in enumerate(self.user_file):
            self.accounts.insert(i, line)

    def check_user(self, user):
        return user in self.accounts