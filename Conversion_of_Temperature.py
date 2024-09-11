def temp():
    Temp = int(input("Enter the Temperature: "))
    Unit = input("Enter the unit of temperature entered above(in Celsius/Fahrenheit/Kelvin): ")
    Conversion_Unit = input("Enter the unit you want to convert the temperature into(in Celsius/Fahrenheit/Kelvin): ")
# for temperature in celsius:
    if Unit.lower() == "celsius" or Unit.lower() == "c":
        if Conversion_Unit == "Fahrenheit" or Conversion_Unit == "fahrenheit" or Conversion_Unit == "F":
            print(f"{((9 * Temp) / 5) + 32}°F")
        elif Conversion_Unit == "Kelvin" or Conversion_Unit == "kelvin" or Conversion_Unit == "K":
            print(f"{Temp + 273} K")
        elif Conversion_Unit == "Celsius" or Conversion_Unit == "celsius" or Conversion_Unit == "C":
            print("You are here just for fun aren't you?")
        else:
            print(f"Spelling is wrong of {Conversion_Unit}")
# for temperature in fahrenheit:
    elif Unit.lower() == "fahrenheit" or Unit.lower() == "f":
        if Conversion_Unit == "Celsius" or Conversion_Unit == "celsius" or Conversion_Unit == "C":
            print(f"{((Temp - 32) * 5) / 9}°C")
        elif Conversion_Unit == "Kelvin" or Conversion_Unit == "kelvin" or Conversion_Unit == "K":
            print(f"{(((Temp - 32) * 5) / 9) + 273} K")
        elif Conversion_Unit == "Fahrenheit" or Conversion_Unit == "fahrenheit" or Conversion_Unit == "F":
            print("You are here just for fun aren't you?")
        else:
            print(f"Spelling is wrong of {Conversion_Unit}")
# for temperature in kelvin:
    elif Unit.lower() == "kelvin" or Unit.lower() == "k":
        if Conversion_Unit == "Celsius" or Conversion_Unit == "celsius" or Conversion_Unit == "C":
            print(f"{Temp - 273}°C")
        elif Conversion_Unit == "Fahrenheit" or Conversion_Unit == "fahrenheit" or Conversion_Unit == "F":
            print(f"{((9 * Temp - 273) / 5) + 32}°F")
        elif Conversion_Unit == "Kelvin" or Conversion_Unit == "kelvin" or Conversion_Unit == "K":
            print("You are here just for fun aren't you?")
        else:
            print(f"Spelling is wrong of {Conversion_Unit}")
# for invalid temperature:
    else:
        print(f"Spelling is wrong of {Unit}")


Ans = "Yes"
while Ans.lower() == "yes":
    temp()
    Ans = input("Do you want to continue: ")
while Ans.lower() == "no":
    print("Thank you for using this program")
    break
else:
    print("Invalid Choice")
