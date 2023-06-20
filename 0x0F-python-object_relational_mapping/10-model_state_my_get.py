#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
parameters given to script: userename, passwd, database, name
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query instances in database
    obj = session.query(State).filter_by(name=argv[4]).first()
    if obj:
        print("{:d}".format(obj.id))
    else:
        print("Not found")

    session.close()
