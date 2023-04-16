#!/usr/bin/python3
"""
 Takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa
 where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection to the database
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SQL query to retrieve states
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))

    # Print the results
    results = cur.fetchall()
    for state in results:
        print(state)

    # Close the cursor and connection
    cur.close()
    conn.close()
