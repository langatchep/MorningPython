#A python program that prompts a user to enter
# a number and checks whether the number is
#even or odd.

number = int(input("Enter a whole number: "))
if (number % 2) == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd")


print("Invalid input. Please enter a valid whole number.")

