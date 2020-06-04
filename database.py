import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()

cur.execute("""
CREATE TABLE if not exists RECORDS (
    name text,
    score integer
)
""")

def insert_result(name, score):
    cur.execute("""
        insert into RECORDS values (?, ?) 
""", (name, score))
    bd.commit()

def get_best():
    cur.execute("""
    select name, max(score) from RECORDS
    GROUP BY name
    ORDER BY score desc
    limit 3
    """)
    return cur.fetchall()

print(get_best())


