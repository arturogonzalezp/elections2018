import os

ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')
FILE_NAME = 'users.txt'

class Accounts:

    def __init__(self):
        self.accounts = []
        try:
            user_file = open(ROOT(FILE_NAME), "r")
        except IOError:
            print ("Cannot open " + FILE_NAME)
        else:
            for i, line in enumerate(user_file):
                self.accounts.insert(i, line)

            user_file.close()

    def check_user(self, user):
        return user in self.accounts