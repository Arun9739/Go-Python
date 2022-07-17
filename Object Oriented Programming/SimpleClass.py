
# This is basic class program which demonstrates the constructor and objects

class Student:
    # constructor
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def display(self):
        print("The student name is : ", self.name)
        print("The student roll number is : ", self.rollNo)


def main():
    s = Student("Arun", 20)
    s.display()


if __name__ == "__main__":
    main()

