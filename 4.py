while True:
    try:
        year = int(input("Enter a year: "))
        if year % 400 == 0 or year % 400 == 0 and year % 100 != 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")
