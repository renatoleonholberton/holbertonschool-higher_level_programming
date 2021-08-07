#!/usr/bin/python3
""" This script connects to a db and executes a query  """

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

    state = state.replace("'", "")

    sql = """
        SELECT ct.id, ct.name, st.name
        FROM states st
        INNER JOIN cities ct
        ON st.id = ct.state_id
        WHERE st.name = '{:s}'
        ORDER BY ct.id ASC
    """.format(state)

    c = db.cursor()
    c.execute(sql)
    cities = c.fetchall()
    print(', '.join([ct[1] for ct in cities]))
    c.close()

    db.close()
