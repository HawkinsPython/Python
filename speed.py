# class Pokemon:
#     def __init__(self, name, pokemon_type, level):
#         self.name = name
#         self.type = pokemon_type
#         self.level = level
#         self.hp = level * 10
#         self.attack_power = level * 2
        
#     def attack(self, target):
#         damage = self.attack_power
#         target.hp -= damage
#         print(f"{self.name} attacked {target.name} for {damage} damage.")
    
#     def heal(self):
#         self.hp = self.level * 10
#         print(f"{self.name} has been healed to full health.")
    
#     def __str__(self):
#         return f"{self.name} - Type: {self.type}, Level: {self.level}, HP: {self.hp}, Attack Power: {self.attack_power}"
    
# # create two Pokemon objects
# pokemon1 = Pokemon("Pikachu", "Electric", 5)
# pokemon2 = Pokemon("Charmander", "Fire", 4)

# # print the details of the Pokemon
# print(pokemon1)
# print(pokemon2)

# # Pikachu attacks Charmander
# pokemon1.attack(pokemon2)
# print(pokemon2)

# # Charmander heals itself
# pokemon2.heal()
# print(pokemon2)

# import random

# pokemon = [
#     {"name": "Bulbasaur", "type": "Grass"},
#     {"name": "Charmander", "type": "Fire"},
#     {"name": "Squirtle", "type": "Water"},
# ]

# player_pokemon = random.choice(pokemon)
# enemy_pokemon = random.choice(pokemon)

# print("A wild", enemy_pokemon["name"], "appeared!")

# while True:
#     print("Your Pokemon:", player_pokemon["name"], "(Type:", player_pokemon["type"], ")")
#     print("Enemy Pokemon:", enemy_pokemon["name"], "(Type:", enemy_pokemon["type"], ")")
    
#     player_choice = input("Choose a move (1. Attack, 2. Switch Pokemon): ")
    
#     if player_choice == "1":
#         if player_pokemon["type"] == enemy_pokemon["type"]:
#             print("It's a draw!")
#         elif (player_pokemon["type"] == "Grass" and enemy_pokemon["type"] == "Water") or \
#             (player_pokemon["type"] == "Fire" and enemy_pokemon["type"] == "Grass") or \
#             (player_pokemon["type"] == "Water" and enemy_pokemon["type"] == "Fire"):
#             print("You win!")
#             break
#         else:
#             print("You lose!")
#             break
#     elif player_choice == "2":
#         player_pokemon = random.choice(pokemon)
#         print("You switched to", player_pokemon["name"])
#     else:
#         print("Invalid choice")
