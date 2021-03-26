#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    myuser = argv[1]
    mypass = argv[2]
    mydata = argv[3]
    argument = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=myuser,
                         passwd=mypass, db=mydata)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name='{}' ORDER BY cities.id;".format(argument))
    r = cursor.fetchall()
    a = ""
    for x in r:
        for y in x:
            print("{}{}".format(a, y), end="")
            a = ", "
    print()
    cursor.close()
    db.close()
