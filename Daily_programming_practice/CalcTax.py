
# This program calculates the tax for given amount

amt = float(input('Enter the amount : '))

tax_rate = float(input('Enter the tax rate in percent : '))

tax_rate /= 100;

print("\nThe tax is : ", amt * tax_rate)