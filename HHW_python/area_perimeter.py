#3)   A programme to display a menu for calculating the area or perimeter of a circle. 

while True:
    a = input("""Program : Input:
1 for Perimeter of circle.
2 for Area of circle.
q to exit.
You: """)
    if a == "q":
        print("Exiting...")
        break

    try:
        a = int(a)

        radius = float(input("Enter the radius of the circle: "))

        perimeter = 2 * 3.142 * radius
        area = 3.142 * radius * radius 

        if a == 1:
            print("Perimeter =", perimeter)
            print("-----------------------------")
        elif a == 2:
            print("Area =", area)
            print("------------------------------")
        else:
            print("Invalid choice. Please enter 1, 2, or q to exit.")
            print("------------------------------")

    except ValueError as e:
        print(f"Enter a valid number for the menu choice and radius, or q to exit: {e}")
        print("-----------------------------------")
