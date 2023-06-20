#!/usr/bin/python3
"""
return all table value of cities that matchs state name
parameters give to script: username, password, database, name
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
    cur.execute("SELECT cities.name\
                FROM states\
                INNER JOIN cities ON states.id=cities.state_id\
                WHERE states.name LIKE '%s'\
                ORDER BY cities.id ASC" % (argv[4],))

    # format the output
    print(', '.join(["{:s}".format(row[0]) for row in cur.fetchall()]))
    cur.close()
    db.close()
