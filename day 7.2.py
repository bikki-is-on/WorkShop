# def profile(name, contact, address):
#     print(f"Name: {name}")
#     print(f"Contact: {contact}")
#     print(f"Address: {address}")

# profile("Ram", "98121212", "KTM")   # positional argument
# print("#####################")
# profile(name="Ram", contact="98121212", address="KTM")      # keyword argument



# def product_one(num1, num2):
#     print(num1*num2)

# ans = product_one(10, 12)
# print(f"Answer: {ans}")

#     #***********************************


# def product_two(num1, num2):
#     return(num1*num2)

# ans = product_two(10,12)
# print(f"Answer: {ans}")



#   use of  *args,  **kwargs            #   arguments and keyword-arguments

# def example(*a):
#     print(a)

# example(1,2,3,4,5,6,7)


def example_two(**kwargs):
    print(kwargs)

example_two(name="Bikram", address="Ktm", phone="9851151")

def example_3(*args, **kwargs):
    print(args)
    print(kwargs)
example_3(1,2,3,4,5,name="Bikki", Address="KTM", phone="9851151")       #   yoh chai dictonary ho