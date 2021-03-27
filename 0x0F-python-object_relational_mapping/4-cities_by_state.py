#!/usr/bin/python3
"""
Project: 0x0F-python-object_relational_mapping
Task: 4
Script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=my_user,
                             passwd=my_pass, db=my_db)
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN \
        states on cities.state_id = states.id ORDER BY cities.id ")
        for elements in cur:
            print(elements)
        cur.close()
        db.close()
    except Exception as error:
        print("ERROR: {}".format(error))
