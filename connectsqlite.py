import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sqlite3
from datetime import datetime,timedelta
connec = sqlite3.connect('mua.db')
cursor = connec.cursor()
# cursor.execute("create table sr(rch int, yr int,mo int, flow_out float, mi text)")
release_list = [
    (1, 2012, 1, 146.15, "dg"),
    (2, 1789, 1, 96.18, "gh"),
    (3, 1956, 1, 11.86, "jk"),
    (4, 1456, 1, 49.46, "ty"),
    (5, 1967, 1, 272.13, "rt"),

]
cursor.executemany("insert into sr values(?,?,?,?,?)", release_list)
connec.commit()
sqlres = "select * from sr"
df = pd.read_sql_query(sqlres, connec)

quarters = {1: 'DJF', 2: 'DJF', 3: 'MAM', 4: 'MAM', 5: 'MAM', 6: 'JJA',
            7: 'JJA', 8: 'JJA', 9: 'SON', 10: 'SON', 11: 'SON', 12: 'DJF'}
df = df.set_index(['mo'])
ssndf = df.groupby(['rch', quarters]).mean()
print(ssndf.head(30))
ssndf = ssndf.reset_index()
ssndf.set_index(['rch'])
print(ssndf.head(5))
pivoted = ssndf.pivot(index='rch', columns='mo', values='flow_out')
pivoted.head()
# Plot size to 15" x 7"
matplotlib.rc('figure', figsize=(15, 7))
# Font size to 14
matplotlib.rc('font', size=14)
# Display top and right frame lines
matplotlib.rc('axes.spines', top=True, right=True)
# Remove grid lines
matplotlib.rc('axes', grid=False)
# Set backgound color to white
matplotlib.rc('axes', facecolor='white')

pivoted.plot(
    kind='bar', title='Seasonal Mean Discharge from 1981 to 2010 ($m^3/s$)')

connec.close()
