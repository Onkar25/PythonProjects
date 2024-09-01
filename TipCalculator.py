print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_per = float(tip/100)
bill_tip = (tip_per * bill) + bill
div_people = round((bill_tip / people),2)
print(f"Each person should pay : {div_people}")