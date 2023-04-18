#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create cursor and execute SQL query
    cur = db_conn.cursor()
    query = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows and print them separated by commas
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db_conn.close()
