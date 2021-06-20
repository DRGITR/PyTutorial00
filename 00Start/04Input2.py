# Program for Area of Circle & Area of Square (side**2)

varMessage = """
What do you want to calculate
Press 1 for Area of Circle
Press 2 for Area of Square
"""
varChoice = int(input(varMessage))

if(varChoice == 1):
    varRadius = int(input("\nEnter the Radius: "))
    if(varRadius < 0):
        print("The Radius cannot be Negative")
    else:
        varArea = 3.14 * varRadius * varRadius
        print(f"Area of Circle is {varArea}")
elif(varChoice == 2):
    varSide = int(input("\nEnter Length of Side: "))
    varAreaSquare = varSide * varSide
    print(f"Area of Square is {varAreaSquare}")
else:
    print("Your Choice is Wrong")






