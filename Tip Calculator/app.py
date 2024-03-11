print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
percent_tip2 = percent_tip / 100 * total_bill + total_bill

each_pay = percent_tip2/split
each_pay = round(each_pay,2)
each_pay = "{:.2f}".format(each_pay)

print(f"Each person should pay: ${each_pay}")
