import pyfiglet

print(pyfiglet.print_figlet("Welocme to TM"))

varOptions = """
Choose one of the following options:
1. Add
2. Multiplication
3. Division
"""

varRepeatCounter = 1

def funAdd():
    varA = int(input("Input Variable A: "))
    varB = int(input("Input Variable B: "))
    print(f"Addition of {varA} and {varB} is {varA+varB}\n")
    varRepeatCounter = int(input("Enter 0 for exit and 1 for Continue\n"))
    return varRepeatCounter

def funMul():
    varA = int(input("Input Variable A: "))
    varB = int(input("Input Variable B: "))
    print(f"Multiplication of {varA} and {varB} is {varA*varB}\n")
    varRepeatCounter = int(input("Enter 0 for exit and 1 for Continue\n"))
    return varRepeatCounter

def funDiv():
    varA = int(input("Input Variable A: "))
    varB = int(input("Input Variable B: "))
    print(f"Division of {varA} and {varB} is {varA/varB}\n")
    varRepeatCounter = int(input("Enter 0 for exit and 1 for Continue\n"))
    return varRepeatCounter

while(varRepeatCounter==1):
    varChoice = int(input(varOptions))
    if(varChoice==1):
        varRepeatCounter = funAdd()
    elif(varChoice==2):
        varRepeatCounter = funMul()
    else:
        varRepeatCounter = funDiv()


