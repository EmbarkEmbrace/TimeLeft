Age = input("What is your current age?  I'd like to determine how many days, weeks, and months you have until you turn 90. \n")
Date = 90
X = ((int(Date) - int(Age)) * int(365))
Y = ((int(Date) - int(Age)) * int(52))
Z = ((int(Date) - int(Age)) * int(12))
print("You have " + str(X) +  " days, " + str(Y) + " weeks, and " + str(Z) + " months left until you are " + str(Date) + " years old.")