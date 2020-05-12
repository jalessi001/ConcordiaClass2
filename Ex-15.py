my_list = ["A", "B", "C"]
copied_list_1 = my_list
copied_list_2 = my_list.copy()
index = 0

for a in my_list:

    if a == "B":
        my_list[index] = "X"
    index += 1

i = copied_list_2.index("B")

print(i)

print(my_list)
print(copied_list_1)
print(copied_list_2)