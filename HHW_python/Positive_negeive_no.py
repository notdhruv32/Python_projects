#1)   A programme to input a number and check whether it is positive, negative, or zero. 

while True:
    a = input("Program: Enter the number (q to exit): ")
    if a == "q":
        print("Exiting...")
        break

    try:
        a = int(a)
        if a > 0:
            print("Program: The number is positive.")
        elif a < 0:
            print("Program: The number is negative.")
        elif a == 0:
            print("Program: The number is 0.")
    except ValueError as e:
        print(f"Program: You can only enter a number or 'q' to exit the program correctly.: {e}")