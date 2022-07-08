# # heroes = ['Spider-man', 'Thor', 'Hulk', 'Iron-man', 'Captain America']

# """
# 1. Length of the list
# 2. Add 'black pather' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list
#    first and then add it after 'hulk'
# 4. Now you don't like hulk and thor because they get angry easily :)
#     so you want to remove hulk and thor from the list and replace them with Dr. Strange(because he is cool).
#     Do that in one line of code
# 5. Sort the heroes list in alphabetical order


# """

# heroes = ['Spider-man', 'Thor', 'Hulk', 'Iron-man', 'Captain America']

# print(len(heroes))          # Answer number 1

# heroes.append('Black Panther')
# print(heroes)                       # Answer number 2

# heroes.remove('Black Panther')
# print(heroes)
# heroes.insert(3,'Black Panther')        # Answer number 3
# print(heroes)

# heroes[1:3] = ['Doctor Strange']    # Answer number 4
# print(heroes)

# heroes.sort()       #Answer number 5
# print(heroes)



            # TASK 2

            # Book --> Class
            # page --> Attribute
            # read --> method

# Noun --> object
# adjective --> property, attribute
# verb(action) --> behaviour, method


class book:
    def __init__(self, page):
        self.page = page

    def read(self):
        print(f"{self.page} is being read.")


b = book(78)                      # यो चाहि एउटा object हो !
b.read()

c = book(90)
c.read()
