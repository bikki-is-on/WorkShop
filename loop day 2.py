# # for i in range(1,10):
# #     n = input("Enter num: ")
# #     if n==9:
# #         break
# #     print(n)

# # for i in range(1,10):
# #     n = int(input("Enter num: "))
# #     if n==9:
# #         break
# #     print(n)


username = "r@gmail.com"
password = "123@abcd"

id= input("Enter usename: ")
pw= input("Enter password: ")
while id != username or pw != password:
    id = input("Enter username: ")
    pw = input("Enter Password: ")

else:
    print("Logged in Successfully!")


# a = [(1,2,3),(5,6,7),(8,9,0)]
# total = 0
# for i in a:
#     total+=("".join([str(j) for j in  i]))

# print(total)
