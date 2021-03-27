#!/usr/bin/python3
""" deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""
from model_city import City
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_row = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for c, s in query_row:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
