######IMPORTS########
from setup import *

######VARIABLES######

# The rate at which the simulation updates in years/seconds (from their perspective/from our perspective)
UPTADE_RATE = 1


######GAMELOOP#######
def game_loop():
    global traits
    print("Welcome to CivSim 0.2!")
    print(traits)
    input()
    fluctuate_traits(UPTADE_RATE, 10)
    cramp_trait_values()
    print(traits)
    input()
    print(f"Old Trait Values: {traits}")
    traits = influence_traits(UPTADE_RATE, 0.05, influence, traits)
    cramp_trait_values()
    print(f"New Trait Values: {traits}")

game_loop()