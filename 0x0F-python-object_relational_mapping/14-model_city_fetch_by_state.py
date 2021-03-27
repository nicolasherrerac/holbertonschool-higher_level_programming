#!/usr/bin/python3
""" deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""
from model_city import Base, City
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
    Base.medata.create_all(engine)
    st = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for c, s in st:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
