######IMPORTS########
import inspect
import random
import math
from traits import *

######FUNCTIONS######

#Function to fluctuate the trait values randomly
def fluctuate_traits(time_scale, sigma):
    global traits
    for trait, value in traits.items():
        change = round(random.gauss(0, sigma * time_scale), 2)
        traits[trait] = value + change
    
#Function to determin the change on influenced traits
def influence_traits(time_scale, influence_scale, influence, traits):
    delta = {}
    for trait in traits:
        delta[trait] = 0

    for source_trait in traits:
        source_value = traits[source_trait] / 100
        for influenced_trait in influence[source_trait]:
            influence_value = influence[source_trait][influenced_trait]

            delta[influenced_trait] += source_value * influence_value * influence_scale * time_scale * 100

    for trait in traits:
        traits[trait] += delta[trait]
    return traits



def cramp_trait_values():
    global traits
    for trait, value in traits.items():
        if value > 100:
            traits[trait] = 100
        elif value < 0:
            traits[trait] = 0