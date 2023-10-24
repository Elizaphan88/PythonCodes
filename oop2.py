class Students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def display(self):
        print("Name: %s \nCourse: %s \nGender: %s \nAge: %d"
              % (self.name, self.course, self.gender, self.age))


stud1 = Students("Elizaphan Maina", "Computer science", "Male", 22)
stud2 = Students("Tabitha Wanjiku", "Geospatial Engineering", "female", 21)

stud1.display()
stud2.display()
