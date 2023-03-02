from pymysql import Connection

connection = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    # db='python_database',
    autocommit=True
)
cur = connection.cursor()
connection.select_db("python_database")
res = cur.execute("SELECT * FROM user")
print(res)
connection.close()
