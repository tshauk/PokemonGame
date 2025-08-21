import random

class player:
    gender = ""
    name = ""
    party = []
    money = 0
    pc = []

    def __init__(self, gender, name, party, money, pc):
        self.gender = gender
        self.name = name
        self.party = party
        self.money = money
        self.pc = pc

    def addParty(self, pokemon):
        if(len(self.party) <6):
            self.party.append(pokemon)
            print(pokemon.name, "was added to your party")
        else:
            self.pc.append(pokemon)
            print("Your party is full.")
            print(pokemon.name, "was sent to your PC")

    def moneyExchange(self,prize):
        self.money += prize

    def display(self):
        print("Name:", self.name)
        print("Your team:")
        for p in self.party:
            if(p.shiny):
                print("Shiny ",p.name, p.level)
            else:
                print(p.name, p.level)
        print("\nYour PC:")
        for p in self.pc:
            if(p.shiny):
                print("Shiny ",p.name, p.level)
            else:
                print(p.name, p.level)

    def getName(self):
        print(self.name)


class pokemon:    
    def __init__(self, name="", level=5, expNeeded=100, expGained=0, moves=None, maxHp=15, hp=15, fainted=False, rarity=2, shiny = False):
        self.name = name
        self.level = level
        self.expNeeded = expNeeded
        self.expGained = expGained
        self.moves = moves if moves is not None else []
        self.maxHp = maxHp
        self.hp = hp
        self.fainted = fainted
        self.rarity = rarity
        self.shiny = shiny
        self.catchRate = self.rarity/3 + 2

    def levelUp(self,leftoverEXP):
        level+=1
        self.expNeeded = 1.15 * self.expNeeded
        self.expGained = leftoverEXP
        
    def takeDamage(self,damage):
        self.hp = self.hp - damage
        if(self.hp < 1):
            self.fainted = True

    def turnShiny(self):
            self.shiny = True
    
    def appears(self):
            
        if (self.shiny == True):
            print("A shiny", self.name, "appeared")
        else:
            print("A", self.name, "appeared")
    
    def randoLevel(self):
        if(self.rarity > 89):
            self.level = 70
        else:
            self.level = random.randint(1,70)

    def reset(self):
        self.catchRate = (self.rarity/3) + 2
        self.randoLevel()
        self.shiny = False
    




def catch(player, pokemon):
    print(player.name, "Threw a pokeball ")
    caught = random.randint(1, pokemon.catchRate) == 1
    if caught == True:
        print(player.name, "caught a ", pokemon.name)
        player.addParty(pokemon)
        pokemon.shiny = False
        pokemon.randoLevel()
    else:
        print("Oh no the pokemon broke free!")
    return caught

def berry(pokemon):
    print("You threw a berry")
    print("The Pokemon is eating")
    if pokemon.catchRate > 1:
        pokemon.catchRate = int(pokemon.catchRate / 2)
    print(pokemon.catchRate)


pokemon_pool = [
    pokemon(name="Rattata", rarity=1),
    pokemon(name="Pidgey", rarity=2),
    pokemon(name="Caterpie", rarity=3),
    pokemon(name="Zubat", rarity=4),
    pokemon(name="Magikarp", rarity=5),
    pokemon(name="Geodude", rarity=6),
    pokemon(name="Oddish", rarity=7),
    pokemon(name="Psyduck", rarity=8),
    pokemon(name="Machop", rarity=9),
    pokemon(name="Tentacool", rarity=10),
    pokemon(name="Charmander", rarity=15),
    pokemon(name="Bulbasaur", rarity=15),
    pokemon(name="Squirtle", rarity=15),
    pokemon(name="Eevee", rarity=20),
    pokemon(name="Growlithe", rarity=22),
    pokemon(name="Vulpix", rarity=22),
    pokemon(name="Sandshrew", rarity=25),
    pokemon(name="Meowth", rarity=25),
    pokemon(name="Poliwag", rarity=28),
    pokemon(name="Abra", rarity=30),
    pokemon(name="Dratini", rarity=35),
    pokemon(name="Scyther", rarity=38),
    pokemon(name="Pinsir", rarity=38),
    pokemon(name="Lapras", rarity=40),
    pokemon(name="Ditto", rarity=42),
    pokemon(name="Togepi", rarity=45),
    pokemon(name="Mimikyu", rarity=48),
    pokemon(name="Riolu", rarity=50),
    pokemon(name="Lucario", rarity=55),
    pokemon(name="Gible", rarity=58),
    pokemon(name="Gabite", rarity=60),
    pokemon(name="Garchomp", rarity=65),
    pokemon(name="Larvitar", rarity=68),
    pokemon(name="Tyranitar", rarity=75),
    pokemon(name="Beldum", rarity=65),
    pokemon(name="Metagross", rarity=75),
    pokemon(name="Axew", rarity=65),
    pokemon(name="Haxorus", rarity=75),
    pokemon(name="Goodra", rarity=75),
    pokemon(name="Hydreigon", rarity=75),
    pokemon(name="Volcarona", rarity=70),
    pokemon(name="Zoroark", rarity=70),
    pokemon(name="Articuno", rarity=91),
    pokemon(name="Zapdos", rarity=92),
    pokemon(name="Moltres", rarity=93),
    pokemon(name="Suicune", rarity=88),
    pokemon(name="Raikou", rarity=88),
    pokemon(name="Entei", rarity=88),
    pokemon(name="Mewtwo", rarity=98),
    pokemon(name="Mew", rarity=99),
    pokemon(name="Arceus", rarity=100)
]



weights = [1 / p.rarity for p in pokemon_pool]

def encounter(player):
    choice = input("Would you like to Catch a Pokemon? 1.Yes or 2.No? ")
    if choice == "1":
        shiny = random.randint(1, 20) == 1
        wildPokemon = random.choices(pokemon_pool, weights=weights, k=6)[0]
        if(shiny):
            wildPokemon.turnShiny()
        wildPokemon.randoLevel()
        wildPokemon.appears()
        caught = False
        while(caught == False):
            enc = input("What would you like to do?\n1. Throw a pokeball\n2.Throw a berry\n3.Run\n")
            if enc == '1':
                caught = catch(player, wildPokemon)
                #return True
            elif enc == "2":
                berry(wildPokemon)
            else:
                print("You got away safely.")
                wildPokemon.reset()
                return True
        return True        
    else:
        player.display()
        return False

# game = True
# print("Hello, welcome to the wonderful world of Pokemon.")
# print("My name is Professor Cedar, I lead the biggest Pokemon Research lab here in the Indus region")
# gender = input("Now tell me, are you a boy or a girl? ")
# name = input("What is your name? ")
# player1 = player(gender,name, [], 0, [])

# while game == True:
# #player1.display() 
#     game = encounter(player1)
    
import tkinter as tk
import random

# Assuming player and pokemon classes are already defined...

class PokemonGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Adventure")
        self.player = None
        self.current_pokemon = None
        self.berry_counter = 0

        # Layout frames
        self.left_frame = tk.Frame(root, width=200, bg="lightgray")
        self.left_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.message_label = tk.Label(self.main_frame, text="", font=("Arial", 12), fg="red")
        self.message_label.pack(pady=5)

        self.setup_start_screen()

    def setup_start_screen(self):
        self.clear_main()
        tk.Label(self.main_frame, text="Welcome to the Pokémon World!", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack()

        tk.Label(self.main_frame, text="Select your gender:").pack()
        self.gender_var = tk.StringVar(value="Boy")
        tk.Radiobutton(self.main_frame, text="Boy", variable=self.gender_var, value="Boy").pack()
        tk.Radiobutton(self.main_frame, text="Girl", variable=self.gender_var, value="Girl").pack()

        tk.Button(self.main_frame, text="Start Adventure", command=self.start_game).pack(pady=10)

    def start_game(self):
        name = self.name_entry.get()
        gender = self.gender_var.get()
        if not name:
            self.message_label.config(text="Please enter your name.")
            return
        self.player = player(gender, name, [], 0, [])
        self.update_team_display()
        self.encounter_screen()

    def encounter_screen(self):
        self.clear_main()
        tk.Label(self.main_frame, text=f"{self.player.name}, would you like to catch a Pokémon?", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.main_frame, text="Yes", command=self.encounter_pokemon).pack()
        tk.Button(self.main_frame, text="No", command=self.show_team).pack()

    def encounter_pokemon(self):
        self.message_label.config(text=" ")
        self.berry_counter = 0  
        self.clear_main()
        shiny = random.randint(1, 256) == 1
        wildPokemon = random.choices(pokemon_pool, weights=weights, k=1)[0]
        if shiny:
            wildPokemon.turnShiny()
        wildPokemon.randoLevel()
        self.current_pokemon = wildPokemon

        text = f"A wild {'Shiny ' if shiny else ''}{wildPokemon.name} appeared! Level {wildPokemon.level}"
        tk.Label(self.main_frame, text=text, font=("Arial", 14)).pack(pady=10)

        tk.Button(self.main_frame, text="Throw Pokéball", command=self.throw_pokeball).pack()
        tk.Button(self.main_frame, text="Throw Berry", command=self.throw_berry).pack()
        tk.Button(self.main_frame, text="Run Away", command=self.run).pack()

    def throw_pokeball(self):
        caught = random.randint(1, int(self.current_pokemon.rarity / 10) + 2) == 1
        if caught:
            self.player.addParty(self.current_pokemon)
            self.message_label.config(text=f"You caught a {self.current_pokemon.name}!")
            self.update_team_display()
            self.encounter_screen()
        else:
            self.message_label.config(text="Oh no! The Pokémon broke free!")
            if self.current_pokemon.name == "Abra":
                self.message_label.config(text="Oh no! The Pokémon broke free!\nThe Pokemon Fled.")
                self.encounter_screen()
            elif self.current_pokemon.rarity < 90:
                run = random.randint(int(self.current_pokemon.rarity),90) == 90
                if run:
                    self.message_label.config(text="Oh no! The Pokémon broke free!\nThe Pokemon Fled.")
                    self.encounter_screen()

    def throw_berry(self):
        if self.berry_counter >= 2:
            self.message_label.config(text="The Pokemon Fled.")
            self.current_pokemon.reset()
            self.encounter_screen()
        else:
            berry(self.current_pokemon)
            self.berry_counter +=1
            self.message_label.config(text=f"The pokemon is eating!")

    def run(self):
         self.message_label.config(text="You got away safely.")
         self.current_pokemon.reset()
         self.encounter_screen()

    def show_team(self):
        self.clear_main()
        tk.Label(self.main_frame, text=f"{self.player.name}'s Team", font=("Arial", 14)).pack(pady=10)

    def update_team_display(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        tk.Label(self.left_frame, text="Your Party", bg="lightgray", font=("Arial", 12)).pack(pady=5)
        for p in self.player.party:
            text = f"{'Shiny ' if p.shiny else ''}{p.name} Lv{p.level}"
            tk.Label(self.left_frame, text=text, bg="lightgray").pack()
        tk.Label(self.left_frame, text="Your PC", bg="lightgray", font=("Arial", 12)).pack(pady=5)
        for p in self.player.pc:
            text = f"{'Shiny ' if p.shiny else ''}{p.name} Lv{p.level}"
            tk.Label(self.left_frame, text=text, bg="lightgray").pack()

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            if widget != self.message_label:
                widget.destroy()


# Run the GUI
root = tk.Tk()
app = PokemonGameGUI(root)
root.mainloop()
