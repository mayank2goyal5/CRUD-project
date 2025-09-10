import mysql.connector
import localadmin,localuser
con=mysql.connector.connect(host="localhost",
                            username="root",
                            passwd="Mayank*107",
                            database="book_my_show")
cur=con.cursor()



def sign_up():
    role=input("please enter role:")
    username=input("enter username")
    password=input("enter password")
    data=(username, password, role)
    query="insert into user(username, password, role)values(%s,%s,%s)"
    cur.execute(query,data)
    con.commit()



def log_in(role):
    username=input("Enter username")
    password=input("enter password")
    query="Select * from user where role=%s"
    data=(role,)
    cur.execute(query,data)
    records=cur.fetchall()
    print(records)
    counter=0
    for i in records:
        if i[1]==username and i[2]==password:
            print("access granted")
            counter=1
            if role=="Admin":
                localadmin.admin_dashboard()
            elif role=="User":
                localuser.user_dashboard(username)
            break
    if counter==0:
       print("invalid creadentails, try again")

            
def menu():
    print("*"*7,"-"*10,"*"*10)
    print("*"*8,"Book My Show","*"*9)
    print("*"*7,"-"*10,"*"*10)

    while True:
       print("Enter")
       print("1 for login as admin")
       print("2 for login as user")
       print("3 for signup")
       choice=int(input("Enter your choice"))

       if choice==1:
        log_in("Admin")
       elif choice==2:
        log_in("User")
       elif choice==3:
        sign_up()
        
if __name__ == "__main__":
     menu()
