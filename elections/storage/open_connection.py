import pymysql

class Connection:
    def connect(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Chanfons_04', db='elections2018',autocommit=True)
        print("Succesful!")
        return conn