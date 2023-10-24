# name = "ELiza"
# for i in name:
#     if i != 0:
#         print(i)

# exceptions handling
fruits = ["mangoes", "apples", "oranges"]
try:
    for i in range(6):
        print(f"The index and element from the list is {i, fruits[i]} ")
except:
    print("Index out of range")

nambari=[3,4,5,7]
if len(nambari)>3:
    raise Exception(f"Length of the given list must be less or equal to 3 but it's {len(nambari)}")
# print(len(nambari))