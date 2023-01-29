import pprint

import pymysql

con = pymysql.connect(
    database="yclients",
    host="sbx01-htz.yclients.tech",
    user="sandbox",
    password="yclients",
    port=3306
)
with con:
    cur = con.cursor()

    cur.execute("select * from users_salons_link where user_id =1")

    rows = cur.fetchall()
    pprint.pp(rows)