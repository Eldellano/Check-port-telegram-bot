import sqlite3


# TODO: generate db, tables
class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('ports.db')
        self.cursor = self.conn.cursor()

    def port_get(self):
        self.cursor.execute('select port, name from net_ports')
        return self.cursor.fetchmany(10)

    def port_add(self, port, name):
        self.cursor.execute('insert into net_ports (port, name) values (?, ?)', [port, name])
        self.conn.commit()

    def port_del(self, port):
        self.cursor.execute('delete from net_ports where port = (?)', [port])
        self.conn.commit()
