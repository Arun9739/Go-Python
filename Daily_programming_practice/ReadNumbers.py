# This program reads 'N' numbers from user and prints them

n = int(input("Enter the number of elements : "))

myList = []

for i in range(0, n):
    item = int(input("Enter the item : "))
    myList.append(item)

print("\nThe entered numbers are : ")
print(*myList, sep = ' --> ')