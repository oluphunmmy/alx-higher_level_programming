#!/usr/bin/python3
"""
first state object from database
parameters given to script: username passwd database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # create engine for database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query instances in database
    obj = session.query(State).order_by(State.id).first()
    if obj:
        print("{:d}: {:s}".format(obj.id, obj.name))
    else:
        print("Nothing")

    session.close()
