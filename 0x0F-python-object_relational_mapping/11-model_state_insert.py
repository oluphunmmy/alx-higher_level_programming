#!/usr/bin/python3
"""Add the state objetc to the database
the script takes: username, passwd, database
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

    # Adding object
    Add = State(name="Louisiana")
    session.add(Add)
    session.commit()

    print("{:d}".format(Add.id))

    session.close()
