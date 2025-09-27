size = int(input("Enter the size of the pattern:"))
temp = size

while size > 0:
    for i in range(temp):
        print("*", end="")
    print()
    size -= 1
