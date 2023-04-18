#!/usr/bin/python3
"""
Connects to a MySQL database,
fetch all rows from the 'states' table,
and filters the results to only include rows
where the 'name' column matches the 'state_name' parameter.
Prints the filtered rows to stdout.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connect to MySQLdb database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    # Create cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SELECT query to fetch all rows from the 'states' table
    cur.execute("SELECT * FROM states WHERE name=%s\
                    ORDER BY id ASC", (sys.argv[4],))

    # Fetch all rows from the SELECT query
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
