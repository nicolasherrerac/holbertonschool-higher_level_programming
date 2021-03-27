#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    st = State(name="Lousiana")
    session.add(st)
    session.commit()
    print(st.id)
    Session().close()
