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
        WHERE name = '{:s}'
        ORDER BY id ASC
    """.format(state)

    with db.cursor() as c:
        c.execute(sql)

        states = c.fetchall()
        for st in states:
            print(st)

    db.close()
