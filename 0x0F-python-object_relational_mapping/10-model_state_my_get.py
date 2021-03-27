#!/usr/bin/python3
"""
    prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa

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
    instanc = session().query(State).filter(State.name == argv[4]).all()
    if instanc:
        for x in instanc:
            if x.name == argv[4]:
                print("{}".format(x.id))
    else:
        print("Not found")
    session().close()
