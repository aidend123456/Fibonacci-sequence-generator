import os
def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

terms = int(input("Enter the number of terms you want: "))
customized = input("Do you want to customize the first two numbers? (y/n): ")
if customized == 'y':
    number1 = int(input("Enter the first number of sequence: "))
    number2 = int(input("Enter the second number of sequence: "))
elif customized == "n":
    number1, number2 = 0, 1

a,b = number1,number2

print(a)
print()
print (b)

for i in range(terms-2):
    a, b = b, a + b
    print()
    print(b)
