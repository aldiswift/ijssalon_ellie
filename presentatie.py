def presenteer(dictionary_2,totaal_bedrag):
    for k, v in dictionary_2.items():
        print(f"{k} : {v} euro")
    print(28 * "=")
    print(f"totaal : {totaal_bedrag} euro")
   
mijn_dict = {
    'vis' : 10, 
    'vlees' : 25, 
    'overig' : 15
    }

totaal = 50