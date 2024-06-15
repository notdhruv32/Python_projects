#2)   A programme to enter a number and check if it is a prime number or not. 

while True:
    a = input("Program: Enter the number (q to exit): ")
    if a == "q":
        print("Exiting...")
        break

    try:
        a = int(a)
        for i in range(2, a):
            if a % i == 0:
                print("The number is composite (not prime).")
                break

        else:
            print("The number is prime.")

    except ValueError as e:
        print(f"Enter 'q' or a valid number: {e}")
