import pymysql
import os

class Connection:
    def __init__(self):
        self.connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                                          port=int(os.environ.get('DB_PORT')),
                                          user=os.environ.get('DB_USER'),
                                          passwd=os.environ.get('DB_PASSWORD'),
                                          db=os.environ.get('DB_SCHEMA'),
                                          autocommit=True)
        self.cursor = self.connection.cursor()