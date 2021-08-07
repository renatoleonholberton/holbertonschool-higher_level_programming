#!/usr/bin/python3
"""Script to change delete all states that contain an 'a' in it's name
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

    res = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()

    for r in res:
        session.delete(r)

    session.commit()
