#!/usr/bin/python3
"""
Project: 0x0F-python-object_relational_mapping
Task: 1
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        for elements in cur:
            print(elements)
        cur.close()
        db.close()
    except Exception as error:
        print("ERROR: {}".format(error))
