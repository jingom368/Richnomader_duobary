import sqlite3
import pandas as pd

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()
cur.execute('SELECT * FROM landing_post')
rows = cur.fetchall()

cols = [column[0] for column in cur.description]

for row in rows:
    df = pd.DataFrame.from_records(data=rows, columns=cols)
df