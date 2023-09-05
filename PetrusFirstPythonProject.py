Name = input("Good day user, may you please insert your name: ")
Weight = int(input("May we please have your current weight, which we'll convert to the desired measuring unit which you desire: "))
Unit = input("Please choose your desired convertable unit.  (S) or (L)bs:  ")

if Unit.upper() == "S":
    convert = Weight / 6.35
    print("Dear " + Name+ "your weight: " + str(convert) + " Stones")
else:
    convert = Weight / 0.45
    print("Name " + Name+ "your weight: " + str(convert) + " Lbs")
