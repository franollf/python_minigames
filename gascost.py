cartype = input("What car are you taking? Type Prius(P), Jaguar(J), Toyota(T), and Honda(H) ").lower()
route = input("Are you taking the highway(H) or through the City(C) ").lower()
destination = input("Where are you going? ")
distance = float(input("How far in KM are you driving? "))
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

if route == "c":
    if cartype == "p": 
     print(f" In the Prius, going to {destination} will cost {literperkm * priusc:.2f}$")
    
    if cartype == "j":
        print(f" In the Jaguar, going to {destination} will cost {literperkm * jaguarc:.2f}$")

    if cartype == "t":
        print(f" In the Toyota, going to {destination} will cost {literperkm * toyotac:.2f}$")

    if cartype == "h":
        print(f" In the Honda, going to {destination} will cost {literperkm * hondac:.2f}$")

if route == "h":
    if cartype == "p":
        print(f" In the Prius, going to {destination} will cost {literperkm * priush:.2f} $")
    if cartype == "j":
        print(f" In the Jaguar, going to {destination} will cost {literperkm * jaguarh:.2f} $")

    if cartype == "t":
        print(f" In the Toyota, going to {destination} will cost {literperkm * toyotah:.2f} $")

    if cartype == "h":
        print(f" In the Honda, going to {destination} will cost {literperkm * hondah:.2f}$")
        