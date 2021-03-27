#!/usr/bin/python3
"""
Project: 0x0F-python-object_relational_mapping
Task: 5
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
        cursor = db.cursor()
        cursor.execute("SELECT cities.name FROM cities JOIN states on cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ", (argv[4],))
        new_list = []
        for elements in cursor:
            new_list.append(elements[0])
        print(", ".join(new_list))
        cursor.close()
        db.close()
    except Exception as error:
        print("ERROR: {}".format(error))
