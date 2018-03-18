import pymysql
import os

class Connection:
    mode = os.environ.get('ENVIRONMENT')
    def __init__(self):
        self.connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                                          port=int(os.environ.get('DB_PORT')),
                                          user=os.environ.get('DB_USER'),
                                          passwd=os.environ.get('DB_PASSWORD'),
                                          db=os.environ.get('DB_SCHEMA'),
                                          autocommit=True)
        self.cursor = self.connection.cursor()

    @staticmethod
    def read_from_file(file_name):
        root = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files/", file_name))
        array = []
        try: 
            file_a = open(root(file_name), "r")
        except IOError:
            print("Cannot open " + file_name)
        else:
            for i, line in enumerate(file_a):
                array.insert(i, "@"+line)
            
            file_a.close()
        return array

    @staticmethod
    def write_to_file(file_name, text):
        root = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files/", file_name))
        try: 
            file_a = open(root(file_name), "w")
        except IOError:
            print("Cannot open " + file_name)
        else:
            file_a.write(text)
            file_a.close()