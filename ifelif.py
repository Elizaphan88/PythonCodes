# when there's more than 1 condition
marks = int(input("Enter marks "))
if marks >= 70 and marks <= 100:
    print("Congrats you scored an A!!")
elif marks >= 60 and marks < 70:
    print("You scored a B!!")
elif marks >= 50 and marks < 60:
    print("You scored a C!!")
elif marks >= 40 and marks < 50:
    print("You scored a D!!")
elif marks < 40:
    print("Sorry uliuma njee")
else:
    print("Invalid!")
