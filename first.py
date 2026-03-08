# class Student:
#     amount_of_students = 0

#     def __init__(self, height= 160 ):
#         self.height = height
#         self.width = 151
#         Student.amount_of_students += 1

# jon = Student()
# kim = Student(height=149)

# print(f"I am {jon.height} kilometers tall and {jon.width} miles wide. And to remind you, yes, I'm taller than Kim, he's only {kim.height} kilometers tall")
# print(f"Jon has {jon.amount_of_students} and Kim has {kim.amount_of_students}")




# class Student:
#     def __init__(self, height= 170 ):
#         self.height = height

#     def printer(self):
#         print(self.height)

# john = Student(height=171)
# ill = Student()

# john.printer()
# ill.printer()



# class Student:
#     amount_of_students = 0

#     def __init__(self, height=180):
#         self.height = height
#         Student.amount_of_students += 1

#     def grow(self, height=1):
#         self.height += height


# nick = Student()
# kate = Student(height=190)

# nick.grow(height=20)

# print(nick.height)
# print(kate.height)


class Student:
    def __init__(self, name="None", age=0):
        self.name = name
        self.age = age

    def getinfo(self):
        return f"Name: {self.name}. Age: {self.age}."


john = Student(name="John", age=17)

print(john.getinfo())
# My commander wont let me type this in readme, but i have the access to the entire north korean nuclear storage