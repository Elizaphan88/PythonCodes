def students(fullname, age, gender, course, school):
    print(f"{fullname} is a {age} years old {gender} pursuing {course} in {school}")


students("Elizaphan Maina", 22, "male", "Bachelors Degree in Geospatial Engineering", "UoN")
students("Tabitha Wanjiku", 21, "female", "Bachelors Degree in Arts", "JKUAT")


def square(num):
    return num ** 2


answer = square(9)
print(f"The square is {answer}")
