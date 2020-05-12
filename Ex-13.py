import random
random_list = [random.randrange(1, 100) for i in range(20)]

print(random_list)

minNum = random_list[0]
maxNum = random_list[0]
countNum = 0
sumNum = 0

for a in random_list:

    if a < minNum:  # to find the minimum number in the list
        minNum = a

    if a > maxNum:  # to find the maximum number in the list
        maxNum = a

    countNum += 1  # to find the number of items in the list

    sumNum = a + sumNum  # to find the sum of all values in list to calculate the average

avgNum = sumNum / countNum  # used to calculate the average of the list

print("The minimum value in the list is %d." % minNum)
print("The maximum value in the list is %d." % maxNum)
print("The number of values in the list is %d." % countNum)
print("The average value in the list is %.2f." % avgNum)

print(min(random_list))
print(max(random_list))
print(len(random_list))
print(sum(random_list)/len(random_list))
