
print("Welcome to Pizza Toppings Rating software. Create a combination of toppings and see how the program reacts to it!")

while True:
    print("Enter 3 toppings like cheese or chicken, etc")
    onet = input("Topping 1:")
    twot = input("Topping 2:")
    threet = input("Topping 3:")


    onet,twot,threet.lower()
    onet,twot,threet.strip()

    topp = (onet,twot,threet)
    toppdict = {'chicken': (3,-3,1), 'cheese': (-3,3,1), 'spices': (8,-5,1), 'jalapeno': (+20,-8,1),'sugar': (-5,8,0), "pineapple": (0,0,0) }
    splvl = 0
    sulvl=0
    edilvl=1
    for topp1 in topp:
        lvl=toppdict[topp1]
        splvl += lvl[0]
        sulvl += lvl[1]
        if "pineapple" in topp:
            edilvl=0

        
    if splvl <9 and sulvl<3 and edilvl ==1:
        print("This Pizza is super good! The people would enjoy this recipe.")

    if splvl>8 and edilvl == 1: 
        print("This Pizza is very spicy! Please reduce the spiciness in the recipe.")

    if sulvl>3 and edilvl == 1:
        print("This Pizza is very sweet! People may get diabetes from eating this Pizza.")
        
    if edilvl == 0:
        print("This is not a pizza. This is a mistake. Do not ever introduce this recipe in a hotel")
    
    yesno = input("Want to try another type of combination? (Y/N):")
    yesno.lower()
    if yesno == "y":
        continue
    else:
        break

