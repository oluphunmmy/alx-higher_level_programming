#!/usr/bin/python3
"""
return all table values of table States with a name starting with N
parameters give to script: username password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # create connection with database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to execute queries using SQl
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for rows in cur.fetchall():
        if (rows[1][0] == 'N'):
            print(rows)
    cur.close()
    db.close()
