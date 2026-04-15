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

#for i in range(0,809):
    #print(data[i]["name"]) #name print
#user = input("Language? English, Japanese, Chinese, or French ").lower() #Ask question

#for i in range(0,809):
    #print(data[i]["name"][user]) #prints what language user wants 

type_ask = input("What Type? ")

new_list = []

for i in range(0,809):
    if data[i]["type"] == 'type_ask':
        print("No Work")


#types = ["Fire","Grass","Steel","Fighting","Water","Bug","Dark",
# "Normal","Psychic","Ice","Ground","Rock","Poison","Fairy","Flying","Ghost","Electric"]


    