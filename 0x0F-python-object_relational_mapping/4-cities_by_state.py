#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username,
mysql password and database name.
"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Connection parameters
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Connection to database
    db_conn = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db
    )

    # Execution of SQL queries
    cursor = db_conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      ORDER BY cities.id ASC""")
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db_conn.close()
