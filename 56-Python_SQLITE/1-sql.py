import sqlite3

# creating and connecting a database
conn = sqlite3.connect("sqlite.db")

# creating a table
conn.execute("""
            
            Create table student(
                st_id INT AUTOINCREMENT PRIMARY KEY,
                st_name VARCHAR(30),
                st_class VARCHAR(10),
                st_email VARCHAR(20)
            )


""")



# closing the connection 
conn.close()