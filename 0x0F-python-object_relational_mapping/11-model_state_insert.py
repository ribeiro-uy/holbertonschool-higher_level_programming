#!/usr/bin/python3
"""
Script that adds the State Lusiana to the database hbtn_0e_6_usa
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
    new_state = State(name='Lusiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
