import mysql.connector
con=mysql.connector.connect(host="localhost", username="root", passwd="Mayank*107",
                            database="book_my_show")
cur=con.cursor()


def insert_data():
    n=int(input("enter how many records do you want to enter"))
    for i in range(n):
        title=input("enter title")
        genre=input("enter genre")
        release_date=input("enter date(yyyy-mm-dd)")
        ticket_price=float(input("enter price"))
        seat_available=int(input("enter seats"))
        data=(title, genre, ticket_price, seat_available, release_date)
        query="insert into movies(title, genre, ticket_price, available_seats, release_date)\
               values(%s,%s,%s,%s,%s)"

        cur.execute(query,data)
        con.commit()


def admin_dashboard():
    print("*"*5,"-"*10,"*"*7)
    print("Welcome Admin")
    print("*"*5,"-"*10,"*"*7)
    while True:
        print("enter 1 for inserting data")
        print("enter 2 for updating data")
        print("enter 3 for deleting data")
        print("enter 4 for reading data")
        print("enter 5 to Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            insert_data()
        elif choice==2:
            update_data()
        elif choice==3:
            delete_data()
        elif choice==4:
            read_data()
        elif choice==5:
            break
               
