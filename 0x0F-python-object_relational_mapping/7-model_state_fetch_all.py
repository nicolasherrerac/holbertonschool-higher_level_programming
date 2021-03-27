#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':

    myuser = argv[1]
    mypass = argv[2]
    mydata = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(myuser, mypass, mydata), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    for instance in session().query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))
    session().close()
