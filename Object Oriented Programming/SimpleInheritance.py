
# This code is to demonstrate the inheritance of classes

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

class Child(Parent):
    def __init__(self, name, usn):
        self.usn = usn
        Parent.__init__(self, name)

    def display(self):
        print(self.name + " " + str(self.usn))

def main():
    a = Parent("Roy")
    b = Child("Naren", 34453)

    a.display()
    b.display()

if __name__ == "__main__":
    main()