#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_city = session.query(State).first()
    if first_city:
        print("{}: {}".format(first_city.id, first_city.name))

"""
   for states in session.query(State).first():
        print("{}: {}".format(states.id, states.name))
    session.close()
"""
