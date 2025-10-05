while True:
    try:
        le_fische_au_chocolat = float(input("Zander's length: "))
        missing_length = 42-le_fische_au_chocolat
        if le_fische_au_chocolat < 0:
            print("Put the damn zander on. There ain't no zander there, don't play with me.")
        elif le_fische_au_chocolat < 42:
            print("We don't hunt no damn kids, release the bastard.\n"
                  f"Them zanders should be {missing_length} centimeters more to be qualified ya heard?")
        else:
            print("goddamn that's a zander alright, hurl it in the ice container")
    except ValueError:
        print("what the hellings cuz, i said input number not letters cuz, boy what da hellll")
    break

