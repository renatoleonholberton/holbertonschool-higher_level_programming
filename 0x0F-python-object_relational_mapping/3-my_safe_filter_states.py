#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, dbname, state = argv[1:]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        host='localhost',
        port=3306,
        db=dbname)

    sql = """
        SELECT *
        FROM states
    """

    c = db.cursor()
    c.execute(sql)
    states = c.fetchall()
    [print(st) for st in states if st[1] == state]
    c.close()

    db.close()
