import sqlite3
db_path = "test-folder/mydatabase.db"

connection = sqlite3.connect(db_path)


# connection.execute(
#     '''INSERT INTO users (username,password) VALUES (?,?)''', ('john', "john123")
# )
# connection.commit()

cursor = connection.execute('''SELECT * FROM users''')
rows = cursor.fetchall()

for row in rows:
    print(row)


connection.close()


#(1, 'john', 'john123')
#(2, 'markus', 'lösen123')
#(3, 'test', 'test')