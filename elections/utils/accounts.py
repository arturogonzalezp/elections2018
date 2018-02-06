class Accounts:
    def __init__(self):
        self.accounts = ["j_alex747", "cesararturo94", "alfonsoirai"]

    def check_user(self, user):
        return user in self.accounts