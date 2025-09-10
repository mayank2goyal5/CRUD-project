import mysql.connector
con=mysql.connector.connect(host="localhost", username="root",
                            passwd="Mayank*107", database="book_my_show")

cur=con.cursor()



def book_ticket(username):
    movie = input("enter movie name :")
    date = input("enter date (yyyy-mm-dd)")
    query = "select * from movies where title = %s "
    data = (movie,)
    cur.execute(query,data)
    record = cur.fetchone()
    movie_id = record[0]
    price = record[3]
    total_seat = record[4]
    query = "select * from booking_availability where \
        movie_id = %s and booking_date = %s "
    data = (movie_id , date)
    cur.execute(query,data)
    records = cur.fetchall()
    print(records)
    if records :
        sum = 0
        for i in records :
            sum = sum + i[4]
        remain = total_seat - sum
        print("Total seat Available : ",remain)   
    else :
        remain = total_seat
        print("Total seat Available : ",remain)
        
    num = int(input("how many :"))
    if num > remain:
        print("not enough seat")
    else:
        print("total price :",price*num)
        choice = input("do u want to continue type 'y':")
        if choice == 'y':
           query = "insert into booking_availability(movie_id,\
               booking_date, total_seats, seats_booked, available_seats, user_name)\
            values (%s,%s,%s,%s,%s,%s)"
           data = (movie_id,date,total_seat,num,remain-num,username)
           cur.execute(query,data)
           con.commit()

           print("ticket booked")
    
           

        else:
           pass

def display_movies():
    query="select *from movies"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print("Movie name-",i[1]," "*3,"genre-",i[2]," "*3,"ticket price-",i[3])
        print()
def user_dashboard(username):
    print("*"*7,"-"*5,"*"*5)
    print(" "*3,"Welcome ",username," "*2)
    print("*"*7,"-"*5,"*"*5)

    while True:
        print("enter 1 to display movie details")
        print("enter 2 for booking a ticket")
        print("enter 3 for cancelling a ticket")
        print("enter 4 to read data")
        print("enter 5 to Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            display_movies()
        elif choice==2:
            book_ticket(username)
        elif choice==3:
            cancel_ticket()
        elif choice==4:
            pass
        elif choice==5:
            break


       
