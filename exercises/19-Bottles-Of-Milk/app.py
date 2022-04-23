def number_of_bottles():
    for value in range(5, -1, -1):
        if value == 1: 
            print(str(value) + " bottle of milk on the wall, " + str(value) + " bottle of milk. Take one down and pass it around, no more bottles of milk on the wall")
        elif value == 0: 
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall")
        else:
            print(str(value) + " bottles of milk on the wall, " + str(value) + " bottles of milk. Take one down and pass it around, " + str(value - 1) + " bottles of milk on the wall")

number_of_bottles()