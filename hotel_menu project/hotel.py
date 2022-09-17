import mysql.connector
import datetime
print("***********HOTEL MANAGEMENT****************")
# CHINESE,ITALIAN,SOUTH INDIA,NORTHINDIA CUISINE,DESSERT,ICECREAM,TEA OR JUICE
# DISH NAME,PRICE(TOTAL BILL),QUANTITY,GST,DATE OF BILL
print("*************DISHES AVAILABILITY*****************")
print("chinese cuisine-Fried rice,Hakka Noodles,Manchurian")
print("south india-Masala dosa,Chapati,parotta gravy-sambar,paneer butter masala,chicken")
print("North india-Aloo parota,Naan,Chole bhature gravy-paneer butter masala,paneer gravy ,channa masala")
print("Dessert-Brownie,Rasagulla,Rasamalai")
print("Icecream-Vanilla,Strawberry,Butterscotch")
menu=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="menu_card"
)
mycursor=menu.cursor()
# mycursor.execute("create database menu_card")
# mycursor.execute("create table menu_items (chinese_dish varchar(255),quantity int,total int)")
# mycursor.execute("create table menu_items2 (southindia_dish varchar(255),gravy varchquantity int,total int)")
# mycursor.execute("create table menu_items3  (northindia_dish varchar(255),gravy varchar(255),quantity int,total int)")
# mycursor.execute("create table menu_items4 (sweet varchar(255),quantity int,total int)")
# mycursor.execute("create table menu_items5 (icecream_flavour varchar(255),quantity int,total int)")
user=input("Enter the type of cuisine you prefer:").lower()
def food_order1(chinese_dish,quantity):
    def insert_data(chinese_dish,quantity,total):
        sql="insert into menu_items(chinese_dish,quantity,total) values (%s,%s,%s)"
        val=(chinese_dish,quantity,total)
        mycursor.execute(sql,val)
        menu.commit()
    if chinese_dish=="fried rice":
        price=100
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {chinese_dish} for {quantity} members is rs.{total} on {date} ( bill is generated along with gst of 18%)")
        insert_data(chinese_dish,quantity,total)
    elif chinese_dish=="hakka noodles":
        price=150
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {chinese_dish} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")
        insert_data(chinese_dish,quantity,total)
    elif chinese_dish=="manchurian":
        price=200
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {chinese_dish} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")  
        insert_data(chinese_dish,quantity,total)
def food_order2(southindia_dish,gravy,quantity):
    def insert_data(southindia_dish,gravy,quantity,total):
        sql="insert into menu_items2 (southindia_dish,gravy,quantity,total) values (%s,%s,%s,%s)"
        val=(southindia_dish,gravy,quantity,total)
        mycursor.execute(sql,val)
        menu.commit()
    if southindia_dish=="parotta" and gravy=="chicken":
        price=198
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {southindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")  
        insert_data(southindia_dish,gravy,quantity,total)
    elif southindia_dish=="chapati" and gravy=="paneer butter masala":
        price=200
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {southindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")  
        insert_data(southindia_dish,gravy,quantity,total)
    elif southindia_dish=="masala dosa" and gravy=="sambar":
        price=150
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {southindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")  
        insert_data(southindia_dish,gravy,quantity,total)
def food_order3(northindia_dish,gravy,quantity):
    def insert_data(northindia_dish,gravy,quantity,total):
        sql="insert into menu_items (northindia_dish,gravy,quantity,total) values (%s,%s,%s,%s)"
        val=(northindia_dish,gravy,quantity,total)
        mycursor.execute(sql,val)
        menu.commit()
    if northindia_dish=="aloo parota" and gravy=="paneer butter masala":
        price=230
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {northindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members") 
        insert_data(northindia_dish,gravy,quantity,total)
    elif northindia_dish=="naan" and gravy=="paneer gravy":
        price=300
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {northindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")   
        insert_data(northindia_dish,gravy,quantity,total)
    elif northindia_dish=="chole bhature" and gravy=="channa masala":
        price=280
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {northindia_dish} and {gravy} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")  
        insert_data(northindia_dish,gravy,quantity,total)           
def food_order4(sweet,quantity):
    def insert_data(sweet,quantity,total,date):
        sql="insert into menu_items2 (sweet,quantity,total,date) values (%s,%s,%s,%s)"
        val=(sweet,quantity,total,date)
        mycursor.execute(sql,val)
        menu.commit()
    if sweet=="brownie":
        price=285
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {sweet} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members") 
        insert_data(sweet,quantity,total,date) 
    elif sweet=="rasagulla":
        price=160
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {sweet} is {total} on {date} ( bill is generated along with gst of 18%) for {quantity} members")
        insert_data(sweet,quantity,total,date)
    elif sweet=="rasamalai":
        price=150
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {sweet} is {total} on {date}") 
        insert_data(sweet,quantity,total,date)                
def food_order5(icecream_flavour,quantity):
    def insert_data(icecream_flavour,quantity,total,date):
        sql="insert into menu_items (icecream_flavour,quantity,total,date) values (%s,%s,%s,%s)"
        val=(icecream_flavour,quantity,total,date)
        mycursor.execute(sql,val)
        menu.commit()
    if icecream_flavour=="vanilla":
        price=110
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.datetime.now()
        print(f"The bill for {icecream_flavour} is {total} on {date} for {quantity} members") 
        insert_data(icecream_flavour,quantity,total) 
    elif icecream_flavour=="butterscotch":
        price=130
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.date.now()
        print(f"The bill for {icecream_flavour} is {total} on {date} for {quantity} members")
        insert_data(icecream_flavour,quantity,total)
    elif icecream_flavour=="strawberry":
        price=120
        cost=price*quantity
        total=cost+(cost*(18/100))
        date=datetime.date.now()
        print(f"The bill for {icecream_flavour} is {total} on {date} for {quantity} members")
        insert_data(icecream_flavour,quantity,total)  
if user=="chinese":
    chinese_dish=input("Enter the item you prefer:")
    quantity=int(input("Enter the quantity of dish:"))
    food_order1(chinese_dish,quantity)
elif user=="southindia":
    southindia_dish=input("Enter the item you prefer:")
    gravy=input("Enter the gravy you prefer:")
    quantity=int(input("Enter the quantity of dish:"))
    food_order2(southindia_dish,gravy,quantity)
elif user=="northindia":
    northindia_dish=input("Enter the item you prefer:")
    gravy=input("Enter the gravy you prefer:")
    quantity=int(input("Enter the quantity of dish:"))
    food_order3(northindia_dish,gravy,quantity)
elif user=="dessert":
    sweet=input("Enter the sweet you prefer:")
    quantity=int(input("Enter the quantity of dish:"))
    food_order4(sweet,quantity)
elif user=="icecream":
    icecream_flavour=input("Enter the icecream flavour you prefer:")
    quantity=int(input("Enter the quantity of dish:"))
    food_order5(icecream_flavour,quantity)
else:
    print("No such dishes are here")
       

