from PIL import Image
print("Welcome to Pizza Toppings Rating software. Create a combination of toppings and see how Vadivelu reacts to it!")

while True:
    print("Enter 3 toppings like cheese or chicken, etc")
    onet = input("Topping 1:")
    twot = input("Topping 2:")
    threet = input("Topping 3:")


    onet,twot,threet.lower()
    onet,twot,threet.strip()

    topp = (onet,twot,threet)
    toppdict = {'chicken': (3,-3,1), 'cheese': (-3,3,1), 'spices': (8,-5,1), 'jalapeno': (+20,-8,1),'sugar': (-5,8,0), "sewage": (0,0,0) }
    splvl = 0
    sulvl=0
    edilvl=1
    for topp1 in topp:
        lvl=toppdict[topp1]
        splvl += lvl[0]
        sulvl += lvl[1]
        if "sewage" in topp:
            edilvl=0

        
    if splvl <9 and sulvl<3 and edilvl ==1:
        img = Image.open("heavenly_pizza.jpg")
        img.show()

    if splvl>8 and edilvl == 1: 
        img = Image.open("spicy.gif")
        img.show()

    if sulvl>3 and edilvl == 1:
        img = Image.open("diabetes.png")
        img.show()
        
    if edilvl == 0:
        img = Image.open("inedible.jpg")
        img.show()
    
    yesno = input("Want to try another type of combination? (Y/N):")
    yesno.lower()
    if yesno == "y":
        continue
    else:
        break

