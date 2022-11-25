import sqlite3
import pandas as pd
from random import uniform, choice
import time
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

connection = sqlite3.connect('time.db')
cursor = connection.cursor()

sqlres = "SELECT datetime(Timestamp) as date, Temperature FROM Temperature"
# tf = cursor.execute(sqlres)
# tf = dict(tf)
# print(tf)
df = pd.read_sql_query(sqlres, connection)
# df.set_index("date", inplace=True)
print(df.head())


# tg = pd.read_sql_query("SELECT datetime(Timestamp) as date FROM Temperature",connection)

x =np.array(list(df["date"].values)) 
y=np.array(list(df["Temperature"].values) )
print(type(y[5]))
plt.xticks(rotation=45)

plt.plot(x[1:5],y[1:5] )
plt.show()
# cursor.execute(
#     "CREATE TABLE Temperature (Timestamp DATETIME NOT NULL, Temperature NUMERIC NOT NULL)")
# cursor.execute("CREATE UNIQUE INDEX idx_timestamp ON Temperature (Timestamp);")
release_list = [
    (1, 1900, "con cho nay"),
    (2, 1459, "con meo nay"),
    (3, 1679, "con lon nay"),
    (4, 1367, "con muoi nay"),
    (5, 1299, "con bo nay")
]
hun = {
    1900: "ty",
    1459: "suu",
    1679: "dan",
    1367: "dau",
    12900: "hoi"
}
# def  dt(days):
#     return timedelta(days=days)
# N_rows=20
# now=datetime.now()
# for i in range(N_rows):
#     timestamp = now - dt(days=(N_rows-i))
#     temperature = uniform(18, 26)
#     cursor.execute("INSERT INTO Temperature VALUES (?, ?)",[timestamp,temperature])
# # cursor.executemany("insert into bl values(?,?,?)", release_list)
# connection.commit()
# mp = df.groupby(['yr']).mean()
# print(mp.head())
connection.close()
