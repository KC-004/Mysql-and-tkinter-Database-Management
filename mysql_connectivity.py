
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kc_db'
)

mycursor = mydb.cursor()

def add_data():

    mycursor = mydb.cursor()
    id = int(input("Enter your id : "))
    name = str(input("Enter your name : "))
    city = str(input("Enter the city name : "))
    phone = int(input("Enter the phone number : "))

    qry = 'INSERT INTO INFO (id, name, city, phone) VALUES(%s, %s, %s, %s)'
    val = [id, name, city, phone]

    mycursor.execute(qry, val)
    print("Data successfully added!")


def get_all_data():

    mycursor = mydb.cursor()

    qry = 'SELECT * FROM info'

    mycursor.execute(qry)
    print("TABLE : INFO")
    for x in mycursor:
        print(x)


def get_specific_data():

    mycursor = mydb.cursor()

    print("Get details by:\n1. Id\n2. Name\n3. City")
    choice = int(input("Enter your choice : "))
    try:
        if choice==1:
            id = int(input("Enter the ID : "))
            qry = 'SELECT * FROM info WHERE id = %s'
            val = [id]
            mycursor.execute(qry, val)

        elif choice==2:
            name = str(input("Enter the Name : "))
            qry = 'SELECT * FROM info WHERE name = %s'
            val = [name]
            mycursor.execute(qry, val)
        elif choice==3:
            city = str(input("Enter the ID : "))
            qry = 'SELECT * FROM info WHERE city = %s'
            val = [city]
            mycursor.execute(qry, val)
        else:
            print("Enter the right choice!")

        for item in mycursor:
            print(item)
    except:
        print("Retry!")


def delete_specific_data():
    get_all_data()
    mycursor = mydb.cursor()

    print("DELETE details by:\n1. Id\n2. Name\n3. City")
    choice = int(input("Enter your choice : "))
    try:
        if choice == 1:
            id = int(input("Enter the ID : "))
            qry = 'DELETE  FROM info WHERE id = %s'
            val = [id]
            mycursor.execute(qry, val)

        elif choice == 2:
            name = str(input("Enter the Name : "))
            qry = 'DELETE  FROM info WHERE name = %s'
            val = [name]
            mycursor.execute(qry, val)
        elif choice == 3:
            city = str(input("Enter the ID : "))
            qry = 'DELETE  FROM info WHERE city = %s'
            val = [city]
            mycursor.execute(qry, val)
        else:
            print("Enter the right choice!")

        get_all_data()
        
    except:
        print("Retry!")


def update_data():

    get_all_data()

    mycursor = mydb.cursor()
    print('Update:\n1. Name\n2. city\n3. phone number')
    choice = int(input("Enter your choice : "))
    id = int(input("Enter the Id : "))

    if choice==1:
        new_name = str(input("Enter the new name : "))
        gry = 'UPDATE info SET name = %s where id=%s'
        val = [new_name, id]
        mycursor.execute(gry, val)

    elif choice==2:
        new_city = str(input("Enter the new city : "))
        gry = 'UPDATE info SET city = %s where id=%s'
        val = [new_city,id]
        mycursor.execute(gry, val)

    elif choice==3:
        new_phone = int(input("Enter the new phone number : "))
        gry = 'UPDATE info SET phone = %s where id=%s'
        val = [new_phone, id]
        mycursor.execute(gry, val)

    else:
        print("Enter the right choice.")

    get_all_data()


update_data()



















