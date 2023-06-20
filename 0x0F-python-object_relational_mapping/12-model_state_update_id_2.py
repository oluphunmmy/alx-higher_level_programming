#!/usr/bin/python3
""" Update a state
The scriptshould take: username, passwd, database
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

    # Updating a state
    update = session.query(State).filter_by(id=2).first()
    update.name = "New Mexico"

    session.commit()
    session.close()
