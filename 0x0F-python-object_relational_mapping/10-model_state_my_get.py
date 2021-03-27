#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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
    state_id = session.query(State).filter_by(name=argv[4]).first()
    if state_id:
        print(state_id.id)
    else:
        print("Not found")
    session.close()
