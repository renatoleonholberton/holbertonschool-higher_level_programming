#!/usr/bin/python3
""" This file connects to a db and executes a query  """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, dbname = argv[1:]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        host='localhost',
        port=3306,
        db=dbname)

    sql = """
        SELECT *
        FROM states
        ORDER BY id ASC
    """

    c = db.cursor()
    c.execute(sql)
    [print(state) for state in c.fetchall()]
    c.close()

    db.close()
