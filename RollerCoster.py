height =int( input("What is your height ?"))
if(height>120):
    print("Your are allowed to ride")
    age = int(input("Whats your age ?"))
    bill = 0
    if(age<12):
        # print("Please pay Rs. 20")
        bill += 20
    elif (age<18):
        # print("Please pay Rs. 30")
        bill += 30
    else:
        # print("Please pay Rs. 50")
        bill += 50
    if(age >= 45 and age <=55):
        bill = 0
    else:
        photo = input("Do you want to take photo (Y for Yes and N for No)")    
        if(photo == 'y'):
            bill += 5
    if(bill == 0):
        print("Enjoy Midlife Crisis Offer !!! \nFREE FREE FREE RIDE")
    else:
        print(f"Please pay Rs. {bill}")

else:
    print("You are not allowed")
print("Enjoy ride !!!")