#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


try:
    db_connect = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
except MySQLdb.error:
    print("Can't connect to Database")
else:
    print("Connected")

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM 'states'")

    [print(state) for state in cursor.fetchall()]
