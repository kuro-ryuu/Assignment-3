while True:
    try:
        bs = input("What's your biological sex?: ").capitalize().strip()
        HV = float(input("Please enter your hemoglobin value (g/1): "))
        if bs == "Female":
            if HV < 117:
                print("Your hemoglobin value is too low.")
            elif HV > 155:
                print("Your hemoglobin value is too high.")
            else:
                print("Your hemoglobin value is normal.")
        elif bs == "Male":
            if HV < 134:
                print("Your hemoglobin value is too low.")
            elif HV > 164:
                print("Your hemoglobin value is too high.")
            else:
                print("Your hemoglobin value is normal.")
        else:
            print("Please enter your biological sex.")
    except ValueError:
        print("Invalid hemoglobin value, please enter a number.")




