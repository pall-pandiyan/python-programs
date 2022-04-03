import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="coder",
    password="coder",
    database="coderdb"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

if ('coderdb',) in mycursor:
    print("Database already exists!")
    #mydb._database = "coderdb"
    #mycursor.execute("SHOW TABLES")
    #[print(x) for x in mycursor]


else:
    mycursor.execute("CREATE DATABASE coderdb")
    mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    
    mydb.commit()


"""

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SHOW TABLES")

[print (x) for x in mycursor]
#for x in mycursor:
#    print(x)

print("Enter the number of lines to be inputed:", end=" ")
n = int(input().strip())
val = []

for i in range(n):
    print("Enter the name to insert:", end=" ")
    name = input().strip()

    print("Enter the address to insert:", end=" ")
    address = input().strip()

    val.append((name,address))

if len(name)<255 and len(address)<255 :
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # val = (name,address)
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "rows entered! ID:", mycursor.lastrowid)


sql = "SELECT name, address FROM customers WHERE address like %s ORDER BY name DESC"
adr = ( "%way%", )

mycursor.execute(sql, adr)
print(mycursor.fetchall())

#[print(x) for x in mycursor.fetchall()]
#for x in mycursor.fetchall():
#    print (x)

"""