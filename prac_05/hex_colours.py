
COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print("The hex code for {} is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    else:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").lower()