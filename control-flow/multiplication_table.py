number = input("Enter a number to see its multiplication table:")
number = int(number)
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
