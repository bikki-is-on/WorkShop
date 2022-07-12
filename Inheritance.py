class User:
    def __init__(self, _id, username, pwd):
        self._id = _id
        self.username = username
        self.pwd = pwd

    def login(self, uname, pwd):
        if self.username == uname and self.pwd == pwd:
            return "Logged In Successfully !"
        return "Unauthorised User"

class Teacher(User):
    def __init__(self, _id, username, pwd, designation):
        super().__init__(_id, username, pwd)
        self.designation = designation

class Student(User):
    def __init__(self, _id, username, pwd, faculty):
        super().__init__(_id, username, pwd)
        self.faculty = faculty

t = Teacher(1, "teacher","teacher","Professor")
s = Student(2, "student", "student", "BCT")
uname = input("Enter username: ")
pwd = input("Enter your password: ")
print(s.login(uname, pwd))
print(t.login(uname, pwd))