#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states from the database
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows and display the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get the MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)

