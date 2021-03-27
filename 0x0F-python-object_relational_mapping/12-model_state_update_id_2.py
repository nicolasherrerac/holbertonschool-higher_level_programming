#!/usr/bin/python3
""" changes the name of a State object from the database hbtn_0e_6_usa
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
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).all()
    for instance in st:
        if instance.id == 2:
            instance.name = "New Mexico"
    session.commit()
    session.close()
