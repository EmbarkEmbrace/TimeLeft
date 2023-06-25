Age = input("What is your current age? I'd like to determine how many days, weeks, and months you have until you turn 90. \n")
Date = 90
Days = 365
Weeks = 52
Months = 12
X = ((int(Date) - int(Age)) * int(Days))
Y = ((int(Date) - int(Age)) * int(Weeks))
Z = ((int(Date) - int(Age)) * int(Months))
print("You have " + str(X) +  " days, " + str(Y) + " weeks, and " + str(Z) + " months left until you are " + str(Date) + " years old.")