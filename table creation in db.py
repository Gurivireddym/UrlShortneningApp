import sqlite3
conn=sqlite3.connect("app.db")

#creating a table in app.db
conn.execute("create table urldb(URL varchar2(1000),shorturl varchar2(100),id number(10)")

#inserting values into urldb table
conn.execute("insert into urldb(url)values('https://github.com/Gurivireddym/Sample_one')");

#deleting all records of urldb table
conn.execute("delete from urldb;")

conn.commit()
conn.close()