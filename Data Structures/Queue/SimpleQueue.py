
# Python program to implement the queue

def enqueue(list):
    item = input("Enter an item : ")
    list.append(item)

def dequeue(list):
    if len(list) == 0:
        print("Queue empty")
    print(list.pop(0))

def display(list):
    print(list)

def main():
    list = []

    while True:
        menuDict = {"1":enqueue, "2":dequeue, "3":display, "4":"EXIT"}
        print("Menu option :")
        print("1.Enqueue \n2.Dequeue \n3.Display \n4.EXIT")

        choice = input("Enter your choice ")
        if choice == "4":
            break

        menuDict[choice](list)


if __name__ == "__main__":
    main()