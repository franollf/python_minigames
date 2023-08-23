# Ask What Car Am I Using
cartype = input("What car are you taking? Type Prius(P), Jaguar(J), Toyota(T), and Honda(H) ").upper()
# Ask am I using the highway or travelling through the city?
route = input("Are you taking the highway(H) or through the City(C) ").lower()
# Ask where am I going?
destination = input("Where are you going? ")
# Ask How Far in KM am i going?
distance = float(input("How far in KM are you driving? "))
# Ask what is the price of Gas?
price = float(input("What is the price of gas right now? "))

literperkm = float(distance) * float(price)

# cars per 100km
priusc = 0.044
priush = 0.046
toyotac = 0.087
toyotah = 0.075
hondac = 0.084
hondah = 0.07
jaguarc = 0.14
jaguarh = 0.102267


def main(x, y):
    print(f" In the {y}, going to {destination} will cost {literperkm * x:.2f}$")

if route == "c":
    if cartype == "P": 
        main(priusc, "Prius")
    
    elif cartype == "J":
        main(jaguarc, "Jaguar")

    elif cartype == "T":
        main(toyotac, "Toyota")

    elif cartype == "H":
        main(hondac, "Honda")
        
    else:
        print("Please enter a valid car type")

if route == "h":
    if cartype == "P":
        main(priush, "Prius")

    elif cartype == "J":
        main(jaguarh, "Jaguar")

    elif cartype == "T":
        main(toyotah, "Toyota")

    elif cartype == "H":
        main(hondah, "Honda")

    else:
        print("Please enter a valid car type")

