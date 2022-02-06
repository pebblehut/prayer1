"""

    prayer.py

    Create prayer database table and load it with initial 
    data

    At any time this file can be run to re-establish a fresh version of the
    database.  It should create a database file called prayer.db.

"""
import sqlite3
import csv

data_sourcefile = 'prayer_test_list.csv'
DROP_PRAYER_SQL = 'DROP TABLE IF EXISTS prayer'
CREATE_PRAYER_SQL = 'CREATE TABLE IF NOT EXISTS prayer (prayerId bigint NOT NULL PRIMARY KEY, prayerText VARCHAR(255), prayerList VARCHAR(63))'
INSERT_RECORD = 'INSERT INTO prayer(prayerId, prayerText, prayerList) VALUES (?,?,?)'

# read data from the file into a list of records
prayer_data = []
try:
    with open(data_sourcefile, encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                prayer_data.append(row)
        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)

prayer_data = prayer_data[1:]
connection = None
try: 
    with sqlite3.connect('prayer.db') as connection:
        cursor = connection.cursor()
        cursor.execute(DROP_PRAYER_SQL)
        cursor.execute(CREATE_PRAYER_SQL)
        # data = (1, "Help my mom", "Family")
        # cursor.execute(INSERT_RECORD, data)
        cursor.executemany(INSERT_RECORD, prayer_data)
        connection.commit()
        print('Data loaded into prayer table.')
        
except sqlite3.Error as err:
    if connection:
        connection.rollback()
        print('data not loaded into prayer table')
        print('Error: {0}'.format(err))
finally:
    if connection:
        connection.close()

