import sqlite3
createDb = sqlite3.connect(':memory:')
queryCurs = createDb.cursor()
queryCurs.execute('''CREATE TABLE inventory 
(number INTRGER, name TEXT, provider TEXT, price REAL, quantity INTEGER)''')


queryCurs.execute('''INSERT INTO inventory(number,name,provider,price,quantity) VALUES(?,?,?,?,?)''',(3200,'Milk','Borden',3.59,1200))
queryCurs.execute('''INSERT INTO inventory(number,name,provider,price,quantity) VALUES(?,?,?,?,?)''',(3201,'Ice cream','Haagen Dazs',5.29,100))
queryCurs.execute('''INSERT INTO inventory(number,name,provider,price,quantity) VALUES(?,?,?,?,?)''',(5632,'Lemon juice','Simply orange',3.49,500))
queryCurs.execute('''INSERT INTO inventory(number,name,provider,price,quantity) VALUES(?,?,?,?,?)''',(23790,'Energy drink','Monster energy',28.99,700))
queryCurs.execute('''INSERT INTO inventory(number,name,provider,price,quantity) VALUES(?,?,?,?,?)''',(23791,'Sprite','CocaCola',12.79,2000)) 
    

print("Exercise a),b)")
queryCurs.execute('SELECT * FROM inventory')
for i in queryCurs:
    print (i)

print(" ")
print("Exercise c)")
queryCurs.execute('''SELECT * FROM inventory WHERE quantity < 1000''')                  
for j in queryCurs:
    print (j)

print(" ")
print("Exercise d)")
queryCurs.execute('''SELECT name,price,quantity FROM inventory ''')                  
for k in queryCurs:
    print (k)

print(" ")
print("Exercise e)")
queryCurs.execute('''SELECT COUNT(*) FROM inventory ''')                  
for l in queryCurs:
    print (l)
createDb.commit()
createDb.close()
print("Exercise f):createDb.commit(), createDb.close() ")


