print("Welcome to Tressure Island.Your mission is to find the tressure.")
input1 = input("You arrive at cross roads.Which path will you take L or R? ")
if input1 == "L":
    input2 = input("You arrive at a river.Will you wait(W) or swim(S)? ")
    if input2 == "W":
        input3 = input(
            "You came across 3 doors,Which one will you choose red(R),green(G) or yellow(Y) "
        )
        if input3 == "Y":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
