first= int(input("Enter the 1st number: "))
second=int(input("Enter the 2nd number: "))
operator=input("Enter the type of operation you want to perform \n\t(+, -, *, /) : ")
sum =0
diff=0
mul=0
div=0
if operator == '+':
    sum = first+second
    print(f"The sum of the given numbers is: ",sum)
elif operator == '-':
    diff = abs(first-second)
    print(f"The difference of the given numbers is: ",diff)
elif operator == '*':
    mul = first * second
    print(f"The product of the given numbers is: ",mul)
elif operator == '/':
    while first>>second:
        div = first/second
        print(f"The divided value of the given numbers is: ",div)
        break
    else:
        div = second/first
        print(f"The divided value of the given numbers is: ",div)
        breakpoint
else:
    print("Syntax Error!!!")
