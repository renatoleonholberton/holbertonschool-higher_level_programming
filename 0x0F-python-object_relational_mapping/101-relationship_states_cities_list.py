#!/usr/bin/python3
"""Script to print all city objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:]

    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(user, passwd, dbname)

    engine = create_engine(conn_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .order_by(State.id)\
        .all()

    for st in states:
        print('{}: {}'.format(st.id, st.name))
        for ct in st.cities:
            print('\t{}: {}'.format(ct.id, ct.name))
