#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connect_db = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=argv[1],
                                 password=argv[2],
                                 database=argv[3],)
    state_name = argv[4]
    cursor = connect_db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities INNER JOIN \
        states ON states.id = cities.state_id \
        WHERE states.name=%(state_name)s ORDER BY cities.id ASC",
        {'state_name': state_name})
    data = cursor.fetchall()
    list_cities = []
    for city in data:
        list_cities.append(city[0])
    print(", ".join(list_cities))
    connect_db.close()
