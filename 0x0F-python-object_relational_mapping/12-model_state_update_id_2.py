#!/usr/bin/python3
"""Script to change the name of a state with id= 2 to 'New Mexico'
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:]

    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(user, passwd, dbname)

    engine = create_engine(conn_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter(State.id == 2)\
        .one()
    state.name = 'New Mexico'

    session.commit()
