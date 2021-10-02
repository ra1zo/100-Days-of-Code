print("!!Thanks for coming to Bla Bla Restaurant!!")
amount = float(input("Your Bill Amount: "))
tip = int(input(
    "Do you mind Tipping our friendly worker: \n Press[1] - Yes \t Press [0] - No \n "))
if (tip > 0):
    tipChoice = float(input(
        "Select Tip Amount : \n Press[1] - 25Rs \t Press [2] - 50Rs \t Press [3] - 100Rs \n "))
    if (tipChoice == 1):
        amount = amount+25
    elif (tipChoice == 2):
        amount = amount+50
    else:
        amount = amount+100
inputs = int(input(
    "!!Bla Bla Restro!!\n Do you prefer Splitting the Bills: \n Press[1] - Yes \t Press [0] - No \n "))

if(inputs == 0):
    print(f"Your Bill amount : {amount} \n Thank you,See you again...")
else:
    persons = int(input("Enter Persons: "))
    total_amount = round(amount/persons, 2)
    print(
        f"Your Bill amount : {amount} \n Each person owes {total_amount} \n Thank you,See you again...")
