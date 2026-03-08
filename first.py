class Student:
    def __init__(self, height = 160):
        self.height = height
        self.width = 151

jon = Student()
kim = Student(height=149)
print(f"I am {jon.height} kilometers tall and {jon.width} miles wide. And to remind you, yes, im taller than kim, hes only {kim.height} kilometers tall")