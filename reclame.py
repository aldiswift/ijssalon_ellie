from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for nr in inkomsten: 
        totaal += nr
    bedrag = totaal * btw 
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden." 

def laag_en_hoog(mijn_lijst):
    laag_en_hoog_lijst = [min(mijn_lijst), max(mijn_lijst)]
    return laag_en_hoog_lijst

def gemiddelde(mijn_lijst):
    gemiddelde_bedrag =  sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."

def hoog_en_laag(mijn_lijst_2):
    uitvoer = laag_en_hoog(mijn_lijst_2)
    uitvoer.reverse()
    return uitvoer

def meervoudig (invoer_lijst):
    uitvoer = hoog_en_laag(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer