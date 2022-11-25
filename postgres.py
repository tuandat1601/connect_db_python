import psycopg2
hostname = "localhost"
port_id = 5432
username = "postgres"
pwd = "tuandat1601"
database = "drv"
# Connect to your postgres DB
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()
    lis = {
        (1, 'dat', 'ely', 'n', '2006-02-14', 'mary.smith@sakilacustomer.org', 'DN'),
        (2, 'luna', 'mu', 'u', '2006-05-19', 'luna.smith@sakilacustomer.org', 'MG'),
        (3, 'mery', 'fib', 'u', '2003-07-20',
         'mery.smith@sakilacustomer.org', 'SN'),
        (4, 'tit', 'mot', 'n', '2001-10-02', 'loy.smith@sakilacustomer.org', 'MJ'),
        (5, 'kato', 'ni', 'u', '2004-09-19', 'been.smith@sakilacustomer.org', 'JH'),
    }

    sqlr = "insert into person values (%s,%s,%s,%s,%s,%s,%s)"
#     cur.executemany(sqlr,lis)

# Execute a query
    cur.execute(
        "select first_name, last_name from person fetch first 2 row only")
    conn.commit()
# Retrieve query results
#     r = cur.fetchall()
    for v in cur.fetchall():
        print(v)
except Exception as err:
    print(err)
finally:

    conn.close()
