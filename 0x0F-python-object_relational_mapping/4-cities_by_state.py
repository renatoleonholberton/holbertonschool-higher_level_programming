#!/usr/bin/python3

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
        SELECT ct.id, ct.name, st.name
        FROM states st
        INNER JOIN cities ct
        ON st.id = ct.state_id
        ORDER BY ct.id ASC
    """

    c = db.cursor()
    c.execute(sql)
    cities = c.fetchall()
    [print(ct) for ct in cities]
    c.close()

    db.close()
