# # Advanced Functions

# #These type of functions are called 'Higher Order Functions'

# # def welcome(name):
# #     print(f"Welcome {name}")

# # def greet_ram(func):
# #     func("Ram")

# # greet_ram(welcome)


# # def square_root_of_sum(func, num1, num2):
# #     return func(num1, num2)**0.5

# # def add(num1, num2):
# #     return num1 + num2

# # print(square_root_of_sum(add, 10 ,15))



# # def outer_function():
# #     def first_child():
# #         print("I am first Child.")
# #     def sec_child():
# #         print("I am second Child.")
# #     sec_child()
# #     first_child()

# # outer_function()



# # def calculator(operator, a, b):
# #     def add():
# #         return a+b
# #     def product():
# #         return a*b

# #     if operator == '+':
# #         return add
# #     elif operator == '*':
# #         return product

# # a= calculator('+', 10, 15)
# # print(a())
# # b= calculator('*', 10, 15)
# # print(b())


# #lambda Function

# # total= lambda a,b:a+b
# # print(total(10,12))

# #map, filter

# #map(func, iterable)

# # a = [1,2,3,4,5]
# # output = []
# # for i in a:
# #     output.append(i+1)

# # print(output)

# # def increment_by_one(n):
# #     return n+1

# # output = map(increment_by_one,a)
# # print(list(output))


# # a = [1,2,3,4,5]
# # def increment_by_one(n):
# #     return n+1

# # output = map(increment_by_one,a)
# # output = map(lambda n:n+1, a)
# # print(list(output))
# # print(a)

# # name =["ram", "shyam", "hari"]
# # print(list(map(lambda s:s.title(),name)))
# # print(list(map(str.title,name)))


# #filter(func, iterable)                               # It is used for boolen functions.

# # a = [1,2,3,4,5]
# # out = list(filter(lambda n: n%2 != 0,a))
# # print(out)


# # Emails = [
# #     "1@gmail.com",
# #     "2@yahoo.com",
# #     "3@gmail.com",
# #     "4@outlook.com",
# #     "5@gmail.com"
# # ]

# # out = list(filter(lambda s:s.endswith("@gmail.com"),Emails))
# # print(out)




# # a= [1, 2, 3, "apple", "Ball", 4, 5, 6]
# # print((filter(lambda n: isinstance(n,int),a)))



# '''
#     1. Class and Objects                Object is physically existance thing and the way of presenting the object is Class
#     2. Inheritance
#     3. Polymorphism
#         -method overriding
#     4. Abstraction
# '''

# class Car:                      # Property and Behaviour
#     def __init__(self, color, model):
#         self.model = model
#         self.color = color

# c = Car("Black", "2022")

# # c.color = "Black"
# print(c.color, c.model)




# def decorate_function(func):
#     def wrapper():
#         print("Hello World !")
#         func()
#         print("Bye Bye world !")
#     return wrapper

# @decorate_function              # Decorator
# def welcome():
#     print("Welcome world !")

# welcome()




# def movie(func):
#     def bujhena():
#         print("K bujhena ?")
#         func()
#         print(" Kina bujhena ?")
#     return bujhena

# @movie
# def kun():
#     print("Kei bujhena")
# kun()

# def smart_function(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "Could not divide"
#         else:
#             return func(a,b)
#     return wrapper

# @smart_function
# def division(a,b):
#     return a/b

# print(division(10,5))
# print(division(10,0))




class Page:
    def __init__(self, page_number, content):
        self.page_number = page_number
        self.content = content

    def read(self):         # Instant Method
        print(f"Reading {self.content} of page number {self.page_number}")

    @staticmethod
    def print_to_printer(content):
        print(f"Printing.....")
        print(content)

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.content


# p = Page(1, "this is new paragraph")
# p.read()
# Page.print_to_printer("This is sentence.")

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def numOfPages(self):
        return len(self.pages)

    def add_page(self, page):
        self.pages.append(page)

    def get_component(self, pageNumber):
        for i in self.pages:
            if i.pageNumber == pageNumber:
                return i.content
        return "Page not found !"

    def __str__(self):
        return self.title

pages = []
for i in range(1,6):
    p =Page(i,f"\nThis is the paragraph {i}")
    pages.append(p)

b = Book("Maths", pages)
#print(f"Number of pages: {b.numOfPages()}")

p = Page(6, "\nThis is a new page.\n")
b.add_page(p)
#print(f"Number of pages: {b.numOfPages()}")

# print(p)
# print(b)
# print(b.pages)

print(b.__dict__)





