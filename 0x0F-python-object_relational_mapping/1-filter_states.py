#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connect_db = MySQLdb.connect(host='localhost',
                                 port=3306, user=argv[1],
                                 password=argv[2],
                                 database=argv[3])
    cursor = connect_db.cursor()
    cursor.execute(
        'SELECT * FROM states WHERE name LIKE \'N%\' ORDER BY states.id ASC')
    data = cursor.fetchall()

    for state in data:
        print(state)

    connect_db.close()
