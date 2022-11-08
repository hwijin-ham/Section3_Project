import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password='hamm1222', db='mysql', charset='utf8')
cur = conn.cursor()


create = """CREATE TABLE review (
    id INT(11) NOT NULL AUTO_INCREMENT, 
    name VARCHAR(20), 
    tags VARCHAR(20), 
    price INT(11), 
    likes VARCHAR(20), 
    score INT(11), 
    CONSTRAINT review_PK PRIMARY KEY(id));"""

cur.execute("DROP TABLE if exists review;")
cur.execute(create)

df = pd.read_csv("/Users/hamhwijin/Section3_Project/selenium/review_modify.csv")

for i in range(len(df)):
    cur.execute("INSERT INTO review (name, tags, price, likes, score) VALUES (%s, %s, %s, %s, %s);", 
            (df["name"][i], df["tags"][i], df["price"][i], df["like"][i], df["score"][i]))

conn.commit()
conn.close()