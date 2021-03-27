#!/usr/bin/python3
"""
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""
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
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'\
        ORDER BY id;".format(argument))
    r = cursor.fetchall()
    for x in r:
        print(x)
    cursor.close()
    db.close()
