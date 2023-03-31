
# This program prints the element of tuple for given index

students = ("arun", "kishor", "yash", "chinmay", "peter", "manish", "prakash", "sushant", "mahendra", "raj")

i = int(input("Enter the element index which you want to retrieve : "))

if i < 0 or i > 9:
    print("Invalid index")
else:
    print("The element is ", students[i])