######IMPORTS########
import inspect
import random
import math
from traits import *

######VARIABLES######
traits = ["trait_religion", "trait_technology"]
trait_values = {}
old_trait_values = {}

######FUNCTIONS######

#Function to fluctuate the trait values randomly
def fluctuate_traits(time_scale):
    global trait_values
    global old_trait_values
    for trait, value in trait_values.items():
        change = round(random.gauss(0, 10 * time_scale), 2)
        trait_values[trait] = value + change

#Runs at the start of the program, generates trait values
def generate_trait_values():
    global trait_values
    for trait in traits:
        trait_values[trait] = 50
    
#Function to determin the change on influenced traits
def influence_trait(trait, influenced_trait, influence_scale, time_scale, old_trait_values):
    global trait_values
    change = old_trait_values[trait] * 0.01 * influence_scale * time_scale
    if change * influence_scale > 0:
        trait_values[influenced_trait] = round(old_trait_values[influenced_trait] + (old_trait_values[influenced_trait] * change), 2)

def cramp_trait_values():
    global trait_values
    for trait, value in trait_values.items():
        if value > 100:
            trait_values[trait] = 100
        elif value < 0:
            trait_values[trait] = 0