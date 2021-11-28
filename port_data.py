import sqlite3


# TODO: generate db, tables
class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('ports.db')
        self.cursor = self.conn.cursor()

    def port_get(self):
        self.cursor.execute('select port, name from net_ports')
        return self.cursor.fetchmany(10)
