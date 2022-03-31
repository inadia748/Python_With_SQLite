import sqlite3

conn = sqlite3.connect('sqlite.db')


# inserting one student
ins = '''

        insert into student(st_name, st_class, st_email) values ('Tony', '12th', 'tony@testing.com')


'''




conn.execute(ins)
conn.commit()
conn.close()