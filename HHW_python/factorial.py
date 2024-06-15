#6)   A python programme to find the factorial of the given number. 

print("This program will tell you the factorial of any number.")
print()
a = int(input("Enter the number: "))

if a == 1 or a == 0:
    print("Facorial = 1")
elif a<0:
    print("factorial for negetive numbers doesn't exist")
elif a>1:
    factorial = 1
    for i in range(1, a+1):
        factorial = factorial * i

print(f"{a}! =", factorial)