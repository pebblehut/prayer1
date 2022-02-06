The Prayer Database app

# Aspirations
An easy way to set reminders to pray - adding in prayer requests to a database, then let the app send reminders from time to time 
* easy entry from iOS/Android device, by email, easily add attachments
* easy management from a web based UI
* strong security - trust that what goes in the DB isn't going to get out to the wrong crowd
* sharing - to other users - export to other contexts - email, reminder in calendar app, printer, social
* point individual requests back to a common attachment (e.g., PDF newsletter) for context
* exponential decay - fewer reminders as time goes by
* snooze - reset the decay
* create prayer list - different weights/rules by prayer list
* prayer cards - (a praying life)
* date based reminders - people on a mission trip, a surgery, etc.

# Current state

prayer.py - create prayer table
prayer_test_list.csv - initial set of test prayers
prayer-fetch.py - test fetching a few results
prayer.db - sqlite3 database
