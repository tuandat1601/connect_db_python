import sqlite3 as lite
import sys

# cur.execute("create table tab (id int, name text, age int, height float, weight float)")
sql_insert = "insert into tab values(?,?,?,?,?)"
tab_item = [
    (1, "dat", 21, 1.67, 66.6),
    (2, "man", 20, 1.7, 56.4),
    (3, "tuyen", 21, 1.62, 64.8),
    (4, "nhan", 20, 1.72, 60.1),
    (5, "truong", 21, 1.66, 53.57),
]
con = lite.connect('demo.db')
# with con:
# 	cur = con.cursor()
# 	sql ="""
# 	update tab
# 	set weight = weight +1
# 	where name = "nhan"
# 	"""
# 	cur.executescript(sql)
# with con:
#     cur = con.cursor()
#     cur.execute("insert into tab values(6,'fa',34,NULL,45)")
#     cur.execute("SELECT * FROM tab")

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)

with con:
    cur = con.cursor()
    cur.execute("BEGIN")
    sql = """
	delete from tab where height is null
	"""
    cur = con.execute(sql)
    cur.execute("rollback")
    cur.execute("SELECT * FROM tab")

    rows = cur.fetchall()

    for row in rows:
        print(row)
con.close()