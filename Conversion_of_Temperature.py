def temp():
    try:
        Temp = int(input("Enter the Temperature: "))
        Unit = input("Enter the unit of temperature entered above(in Celsius/Fahrenheit/Kelvin): ")
        Conversion_Unit = input("Enter the unit you want to convert the temperature into(in Celsius/Fahrenheit/Kelvin): ")
        if Unit.isalpha() == True and Conversion_Unit.isalpha() == True:
        # for temperature in celsius:
            if Unit.lower() == "celsius" or Unit.lower() == "c":
                if Conversion_Unit.lower() == "fahrenheit" or Conversion_Unit.lower() == "f":
                    print(f"{Temp}°C = {((9 * Temp) / 5) + 32}°F")
                elif Conversion_Unit.lower() == "kelvin" or Conversion_Unit.lower() == "k":
                    print(f"{Temp}°C = {Temp + 273}K")
                elif Conversion_Unit.lower() == "celsius" or Conversion_Unit.lower() == "c":
                    print("You are here just for fun aren't you?")
                else:
                    print("Invalid unit entered")
        # for temperature in fahrenheit:
            elif Unit.lower() == "fahrenheit" or Unit.lower() == "f":
                if Conversion_Unit.lower() == "celsius" or Conversion_Unit.lower() == "c":
                    print(f"{Temp}°F = {((Temp - 32) * 5) / 9}°C")
                elif Conversion_Unit.lower() == "kelvin" or Conversion_Unit.lower() == "K":
                    print(f"{Temp}°F = {(((Temp - 32) * 5) / 9) + 273}K")
                elif Conversion_Unit.lower() == "fahrenheit" or Conversion_Unit.lower() == "f":
                    print("You are here just for fun aren't you?")
                else:
                    print("Invalid unit entered")
        # for temperature in kelvin:
            elif Unit.lower() == "kelvin" or Unit.lower() == "k":
                if Conversion_Unit.lower() == "celsius" or Conversion_Unit.lower() == "c":
                    print(f"{Temp}K = {Temp - 273}°C")
                elif Conversion_Unit.lower() == "fahrenheit" or Conversion_Unit.lower() == "f":
                    print(f"{Temp}K = {((9 * Temp - 273) / 5) + 32}°F")
                elif Conversion_Unit.lower() == "kelvin" or Conversion_Unit.lower() == "k":
                    print("You are here just for fun aren't you?")
                else:
                    print("Invalid unit entered")
        # for invalid temperature:
            else:
                print("Invalid unit entered")
        else:
            print("\n\"Invalid unit entered\"")
    except:
        print("\n\"VALID VALUE NOT ENTERED\"")


while True:
    print("\n\"WELCOME TO THE PROGRAM FOR CONVERTING TEMPERATURE UNITS\" \nEnter '1' to proceed \nEnter '2' to exit the program")
    try:
        ch = int(input("Enter the choice: "))
        if ch == 1:
            temp()
        elif ch == 2:
            break
        else:
            print("\n\"VALID CHOICE NOT ENTERED\"")
    except:
        print("\n\"VALID VALUE NOT ENTERED\"")
print("Thank you for using this program :)")
