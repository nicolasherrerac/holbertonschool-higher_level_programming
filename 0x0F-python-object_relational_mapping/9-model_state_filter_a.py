#!/usr/bin/python3
"""
    lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""
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
    instance = session().query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    if instance:
        for x in instance:
            if 'a' in x.name:
                print("{}: {}".format(x.id, x.name))
    session().close()
