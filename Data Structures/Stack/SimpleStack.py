
# This program implements the stack by using a list

myList = []


def pushStack():
    item = int(input("Enter an item to enter : "))
    myList.append(item)


def popStack():
    if len(myList) != 0:
        item = myList.pop(0)
        print(str(item) + " is removed from stack")
    else:
        print("Stack is empty")


def displayStack():
    if len(myList) != 0:
        print("The contents in stack are : ")
        print(*myList, sep = " --> ")
    else:
        print("Stack is empty")

def main():
    print("Program on Implementation of stack : ")

    menu = {"1" : pushStack, "2" : popStack, "3" : displayStack, "4" : "EXIT"}

    while True:
        print("\n1. Push an item  2. Pop an item  3. Display stack  4. EXIT\n")
        choice = input("Enter your choice : ")

        if choice == "4":
            break
        menu[choice]()


if __name__ == "__main__":
    main()

