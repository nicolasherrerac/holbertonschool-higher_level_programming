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
        'mysql+mysqldb://{}:{}@localhost/{}'.format(myuser, mypass, mydata), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    instance = session().query(State).filter(
        State.name == argv[4].all()
    if instance:
        for x in instance:
            if x.name == argv[4]:
                print("{}".format(x.id))
    session().close()
