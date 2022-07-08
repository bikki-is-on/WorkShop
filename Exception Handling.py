
from tokenize import Name


try:
    n1 = int(input("Enter number: "))
    n2 = int(input("Enter number: "))
except ValueError:
    print("Variable not defined")
except NameError:
    print("Variable not defined")
else:
    print(n1 + n2)