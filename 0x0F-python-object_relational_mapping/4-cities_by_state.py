#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connect_db = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=argv[1],
                                 password=argv[2],
                                 database=argv[3],)
    cursor = connect_db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN \
        states ON states.id = cities.state_id ORDER BY cities.id ASC")
    data = cursor.fetchall()

    for citie in data:
        print(citie)

    connect_db.close()
