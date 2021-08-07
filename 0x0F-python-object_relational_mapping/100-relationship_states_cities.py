#!/usr/bin/python3
"""Script to print all city objects
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:]

    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(user, passwd, dbname)

    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    city = City(name='San Francisco')
    city.state = State('California')

    session.add(city)
    session.commit()
