
# This program demonstrates how a Complex number can be represented in a class

class Complex:
    # constructor

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, c):
        temp = Complex(0, 0)
        temp.real = self.real + c.real
        temp.imag = self.imag + c.imag
        return temp

    def subtract(self, c):
        temp = Complex(0, 0)
        temp.real = self.real - c.real
        temp.imag = self.imag - c.imag
        return temp

    def multiply(self, c):
        temp = Complex(0, 0)
        temp.real = self.real * c.real
        temp.imag = self.imag * c.imag
        return temp

    def divide(self, c):
        temp = Complex(0, 0)
        temp.real = (float) (self.real / c.real)
        temp.imag = (float) (self.imag / c.imag)
        return temp

    def display(self):
        print("The real part : " + str(self.real))
        print("The imaginary part : " + str(self.imag))


def main():
    a = Complex(5, 7)
    b = Complex(1, 3)
    res = Complex(0, 0)

    res = a.add(b)
    print("Addition : ")
    res.display()
    print()

    res = a.subtract(b)
    print("Subtraction : ")
    res.display()
    print()

    res = a.multiply(b)
    print("Multiplication : ")
    res.display()
    print()

    res = a.divide(b)
    print("Division : ")
    res.display()
    print()


if __name__ == "__main__":
    main()



