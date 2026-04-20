# Create DONE a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add DONE a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type




import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")       
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

moves = open("./moves.json", encoding="utf8")  
data = json.load(moves)

'''for i in range(0,809):
    print(data[i]["name"]) #name print
user = input("Language? English, Japanese, Chinese, or French ").lower() #Ask question

for i in range(0,809):
    print(data[i]["name"][user]) #prints what language user wants 
for i in range(0,809):
    print(data[i]["name"][user]) 

type_ask = input("What Type? ")'''

'''for pokemon in data:
    if type_ask in pokemon["type"]:
        print(pokemon["name"]["english"])
        Found = True
    else: Found  = False
if Found == False:
    print("Nothing") '''

'''count = 0
name_ask = input("Name Match ")
for char in data:
    if name_ask in char["name"]["english"]:
        print(char["name"]["english"])
        count = 1
if count == 0:
    print("None Was Found")'''





moves = input("Pokemon: ")
for things in data:
    if moves in things["name"]["english"]:
        print(things["type"])


    




    





    
        
        


#types = ["Fire","Grass","Steel","Fighting","Water","Bug","Dark",
# "Normal","Psychic","Ice","Ground","Rock","Poison","Fairy","Flying","Ghost","Electric"]


    