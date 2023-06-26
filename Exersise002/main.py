# list_1 = [1, 2, 3, 4, 5]
# k = 6

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
index = 0
difference = 0
for i in range(0, len(list_1)):
    if i == 0:
        difference = k - list_1[i]

    if abs(k - list_1[i]) < difference:
        index = i
        difference = k - list_1[i]

    if difference == 0:
        break

print(list_1[index])
