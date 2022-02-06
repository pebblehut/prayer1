from collections import namedtuple
from contextlib import closing
import sqlite3

Prayer = namedtuple('Prayer', 'id text list')
prayers3 = []
prayerList = "Family"

try: 
    with closing(sqlite3.connect('prayer.db')) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT prayerId, prayerText, prayerList FROM prayer WHERE prayerList=?', (prayerList,))
        # prayers1 = Prayer(*cursor.fetchone())
        prayers2 = [Prayer(*sch) for sch in cursor.fetchmany(size=3)]

        # for sch in cursor:
            # prayers3.append(School(sch[0])
            # schools3.append(School(sch[0], sch[1], sch[2]))

except sqlite3.Error as e:
    print('Error: {0}'.format(e))

print('Prayers in {0} list'.format(prayerList))
# print('{id} - {text}'.format(id=prayers1.id,
    # text=prayers1.text))
for prayer in prayers2:
    print('{id} - {text}'.format(id=prayer.id,
        text=prayer.text))
