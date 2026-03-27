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

for i in range(0,809):
    print(data[i]["name"])


#user = input("Language? ").lower()

#for i in range(0,809):
    #if user == "english":
       # print(data[i]["name"]["french"])
   # elif user == "japanese":
    #    print(data[i]["name"]["japanese"])
    #else:
    #    print(data[i]["name"]["chinese"])




for i in range(0,809):
    print(data[i]["type"])





#user1= input("Type: ").lower()

#for i in range():
    #if user1 == "steel":

   # if user1 == "electric":
    
    #if user1 == "fire":

   # if user1== "rock":

    #if user1 == "posion":

   # if user1 == "dragon":
    