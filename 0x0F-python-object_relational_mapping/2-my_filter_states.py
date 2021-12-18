#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connect_db = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=argv[1],
                                 password=argv[2],
                                 database=argv[3],)
    searched = argv[4]
    cursor = connect_db.cursor()
    cursor.execute(
        "SELECT states.id, states.name FROM states WHERE name='{}'\
        ORDER BY states.id ASC".format(searched))
    data = cursor.fetchall()

    for state in data:
        print(state)

    connect_db.close()
