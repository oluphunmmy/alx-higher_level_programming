#!/usr/bin/python3
"""
return all table values of table States where name matches the argument.
parameters give to script: username password, database, name
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
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".
                format(argv[4]))
    for rows in cur.fetchall():
        if rows[1] == argv[4]:
            print(rows)
    cur.close()
    db.close()
