# inbuilt data types

# lists mutable,ordered
mylist = ["Erick", "Elizaphan", "Mary", "Gloria", "Brian"]
print(mylist)
print(f"My name is {mylist[1]}")
print(f"My name is " + mylist[1])

mylist2 = [89, 12, 34, 0, 1, 17, 9, -3, -19]
mylist2.sort
print(mylist)
print(f"The third item is " + str(mylist2[2]))
print(f"The third item is  {mylist2[2]}")
print(f"My sorted list is  {mylist2}")

# tuple immutable,ordered
my_tuple = ("kenya", "uganda", "tanzania", ["usa", "russia"], "ethiopia", "burundi", "somalia")
# my_tuple[2]="congo"
print(my_tuple)
print(f"My country is {my_tuple[0]}")

# sets Mutable,unordered,no indices
fruits = {"oranges", "pineapples", "mangoes", "bananas", "apples"}
print(fruits)

# Dictionaries mutable
employees = {"Name": "Elizaphan", "Age": 22, "Gender": "Male", "Salary": 500000}
print(f"Employees name :%s" % employees["Name"])
print(f"Employees age :%d" % employees["Age"])
