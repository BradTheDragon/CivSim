######IMPORTS########
from traits import *

######VARIABLES######

# The rate at which the simulation updates in years/seconds (from their perspective/from our perspective)
UPTADE_RATE = 1


######GAMELOOP#######
def game_loop():
    global trait_values
    global old_trait_values
    generate_trait_values()
    print("Welcome to CivSim 0.1!")
    print(trait_values)
    input()
    fluctuate_traits(UPTADE_RATE)
    print(trait_values)
    input()
    old_trait_values = trait_values.copy()
    print(f"Old Trait Values: {old_trait_values}")
    for trait in traits:
        if trait in influence:
            for influenced_trait, influence_scale in influence[trait].items():
                influence_trait(trait, influenced_trait, influence_scale, UPTADE_RATE, old_trait_values)
    print(f"New Trait Values: {trait_values}")

game_loop()