#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
            db_location='localhost'
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM 'states'")
    results = cursor.fetchall()
    for state in results:
        print(state)
    db_connection.close()
