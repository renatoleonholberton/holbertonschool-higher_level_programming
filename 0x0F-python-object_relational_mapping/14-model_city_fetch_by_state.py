#!/usr/bin/python3
"""Script to print all city objects
"""
import sys
from model_state import State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:]

    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(user, passwd, dbname)

    engine = create_engine(conn_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City)\
        .filter(State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    for st, ct in res:
        print('{}: ({}) {}'.format(st.name, ct.id, ct.name))
