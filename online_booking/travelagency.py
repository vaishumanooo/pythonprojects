# include gst after completion,online offline mode payment (include,avaialbility of agency timimg for both online and offline)
# date=datetime.datetime.now()
import datetime
print("**********TRAVEL AGENCY**************")
print("Foreign travel packages")
print("Singapore-5 days travel expense of 40k")
print("Paris-4 days travel expense of 45k")
print("North India travel packages")
print("Ladakh-5 days travel expense of 25k")
print("Delhi-4 days travel expense of 20k")
print("South India travel packages")
print("Kanyakumari-3 days travel expense of 15k")
print("Ooty-2 days travel expense of 12k")
date=datetime.datetime.now()
print(date)

user=input("Enter the type of package you want:")d
def foreign_travel(location,count):
    if location=="singapore":
        amount=40000
        count=count*amount
        print(f"The total amount for {location} is {count}")
    elif location=="paris":
        amount=45000
        count=count*amount
        print(f"The total amount for {location} is {count}")        
def northindia_travel(location,count):
    if location=="ladakh":
        amount=25000
        count=count*amount
        print(f"The total amount for {location} is {count}")
    elif location=="delhi":
        amount=20000
        count=count*amount
        print(f"The total amount for {location} is {count}") 
def southindia_travel(location,count):
    if location=="kanyakumari":
        amount=15000
        count=count*amount
        print(f"The total amount for {location} is {count}")
    elif location=="ooty":
        amount=12000
        count=count*amount
        print(f"The total amount for {location} is {count}") 
if user=="foreign":
    location=input("Kindly,enter the location available here:")
    count=int(input("Enter the count of people:"))
    foreign_travel(location,count)
elif user=="northindia":
    location=input("Kindly enter the location available here:")
    count=int(input("Enter the count of people:"))
    northindia_travel(location,count)
elif user=="southindia":
    location=input("Kindly enter the location available here:")
    count=int(input("Enter the count of people:"))
    southindia_travel(location,count)    
else:
    print("Kindly check out other website if your package isn't vailable here")


    