#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    myuser = argv[1]
    mypass = argv[2]
    mydata = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=myuser,
                         passwd=mypass, db=mydata)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    r = cursor.fetchall()
    for x in r:
        print(x)
    cursor.close()
    db.close()
