import os
import sqlite3
import pandas as pd

DB_FILENAME = 'review.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS review;")

create = """CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR, 
    tags VARCHAR, 
    price INTEGER, 
    likes VARCHAR, 
    score INTEGER);"""

cur.execute(create)

df = pd.read_csv("/Users/hamhwijin/Section3_Project/selenium/review_modify.csv")

for i in range(len(df)):
    cur.execute("INSERT INTO review (name, tags, price, likes, score) VALUES (?, ?, ?, ?, ?);", 
            (df["name"][i], df["tags"][i], int(df["price"][i]), df["like"][i], int(df["score"][i])))

conn.commit()
conn.close()