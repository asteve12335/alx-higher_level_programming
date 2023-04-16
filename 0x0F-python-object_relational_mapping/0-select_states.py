#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # create connection to our database
    db_connect = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    # Create cursor to execute queries
    cursor = db_connect.cursor()

    # Use cursor to execute queries
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Retrieve results from query
    results = cursor.fetchall()

    # Display each result
    for state in results:
        print(state)

    # Close our cursor
    cursor.close()

    # Close the connection to our database
    db_connection.close()
