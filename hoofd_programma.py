from helper import onderstreep 

uitvoer = onderstreep("ANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liters: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print(el)