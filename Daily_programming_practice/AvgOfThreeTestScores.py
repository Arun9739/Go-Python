
# This program calculates the average of three test scores

print("Enter 3 exam scores")

total = 0
total += int(input("Enter first score : "))
total += int(input("Enter second score : "))
total += int(input("Enter three score : "))

avg = round(total / 3)

print("\nThe total of 3 scores is : ", total)
print("The average of 3 scores is : ", avg)
