list = []
swapped = True
num = int(input("How many elements do you want to sort? "))
for i in range(num):
    val = float(input("Enter next element: "))
    list.append(val)
while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i],list[i + 1] = list[i + 1],list[i]
print("Sorted:")
print(list)