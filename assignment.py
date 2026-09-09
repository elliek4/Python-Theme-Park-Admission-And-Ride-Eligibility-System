# Name: Ellie Khoo
# Period: AM
# Theme Park Admission & Ride Eligibility System

#introduce program to user
print()
print("Welcome to the Python Adventure Park!")
print("Today we will be getting your ticket ready!")
print("Then we'll find out which rides you can go on!")

#get user's info by asking them to input it
print()
guest_name = input("What is your name? ")
age = int(input("What is your age? "))
height = int(input("What is your height in inches? "))
ticket_type = input("Did you purchase a regular or premium ticket? ")
park_member = input("Are you a park member? yes/no ")
visiting_with_adult = input("Are you visiting with an adult? yes/no ")
visiting_time = input("Are you visiting during the morning or evening? ")

#create function to determine admission price
def calculate_admission(guest_age):     #using age as parameter, putting in variable guest_age
    if guest_age >= 65:                 #using if to check what guest's age is and determining admission price based on that
        price = 20
    elif guest_age >= 13:
        price = 30
    elif guest_age >= 5:
        price = 15
    else: 
        price = 0
    return price

admission_price = calculate_admission(age)  #storing returned value inside admission_price

#create function to determine discount
def calculate_discount(price, member, visit_time):    #using price, whether park member or not, and visiting time as parameter
    discount = 0
    if member == "yes" and visit_time == "evening":   #using if to check if guest is eligible for discount and applying it based on visting time and whether park member or not
        discount = 10
    elif visit_time == "evening":
        discount = 3
    elif member == "yes":
        discount = 5

    if price == 0: #if price is 0, no discount will be applied
        discount = 0
    
    return price-discount

discount_price = calculate_discount(admission_price, park_member, visiting_time) #storing returned value inside discount_price

#create function to determine highest ride level the guest qualifies for
def ride_level(guest_age, guest_height): #uses guest's age and height as parameters to determine guest's ride eligibilty
    if guest_age >= 16 and guest_height >= 54: #uses if to check guest's age and height and determines which rides the guest qualifies for
        return "Extreme Rides"
    elif guest_age >= 12 and guest_height >= 48:
        return "Thrill Rides"
    elif guest_age >= 8 and guest_height >= 42:
        return "Family Rides"
    elif guest_height >= 36:
        return "Kiddie Rides"
    else:
        return "No Rides"

riding_level = ride_level(age, height) #stores ride level inside riding_level

#create function to check adult supervision and whether guest is allowed to enter the park
def check_supervision(guest_age, adult_present):
    if guest_age >= 13: #using if to check if the guest is old enough or has adult supervision to determine entry allowance
        return "Approved"
    elif adult_present == "yes":
        return "Approved"
    else:
        return "Adult Required"

park_entry_status = check_supervision(age, visiting_with_adult) #storing quest ability to enter park in park_entry_status 

#check if guest has premium ticket and display eligibility for benefits
premium_status = ""
print()
if ticket_type == "premium":
    print("PREMIUM TICKET: You receive a free snack and priority ride access!")
    premium_status = "yes"
else:
    print("REGULAR TICKET: You are not eligible for any benefits.")
    premium_status = "no"

#create function to check and return if guest has vip or standard status 
def check_vip(ticket, member, guest_age):
    if (ticket == "premium" and member == "yes") or (ticket == "premium" and guest_age >= 65):
        return "VIP ACCESS"
    else:
        return "STANDARD ACCESS"
        
guest_status = check_vip(ticket_type, park_member, age) #stores check_vip of guest's status in guest_status

#display final guest report: calculated information from user input and functions
print()
print("--------------------------------------------")
print("Python Adventure Park Guest Report")
print()
print("Name:", guest_name)
print()
print("Age:", age)
print("Height:", height, "inches")
print("Ticket Type:", ticket_type)
print("Park Member Status:", park_member)
print()
print("Admission Price Before Discount:", f"${admission_price}")
print("Final Admission Price:", f"${discount_price}")
print()
print("Ride Level:", riding_level)
print()
print("Supervision Status:", park_entry_status)
print()
print("Premium Ticket Status:", premium_status)
print("Guest Status:", guest_status)
print("----------------------------------------------")

#closing display statement, including special message to people who can't ride anything
print()
print("Have an awesome time at the park!")
if age < 8: #if guest's age is younger than 8, display personalized message
    print("Come back in a few years so you can ride the extreme rides kiddo!")
print()