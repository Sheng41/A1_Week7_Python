print("Rules that govern the state of water")

# let the user pick a temp, see what happens to water (conditional statements)
# current_temp is the temperature varible(user inputs this)
current_temp = False

while current_temp is False:
    # user input - this changes temp on every iteration
    current_temp = input("Enter a temperature: \n")
    print(current_temp)

    # if it's below 0, obvi it's frozen
    if(int(current_temp) < 0) or (int(current_temp) == 0):
        print("water is a solid. icy")
        current_temp = False

    # if it's between 0 and 100, it's a liquid
    elif (int(current_temp) < 100):
        print("water a liquid. profit!")
        current_temp = False

    # if it's aboe100, obvi it's a gas
    elif (int(current_temp) > 100) or (int(current_temp) == 100):
        print("water is a vapor, cuz it's hot")
        current_temp = False
