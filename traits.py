######IMPORTS########

######VARIABLES######
traits = {}

######FUNCTIONS######

#Runs at the start of the program, to make sure the traits are up to date
def update_trait_list():
    global traits
    traits = [name for name, obj in globals().items() if callable(obj) and name.startswith("trait_")]

#Mainly used to run trait functions
def run_func(function_name, *args, **kwargs):
    try:
        # Get the function from the global scope
        func = globals()[function_name]
        if callable(func):
            return func(*args, **kwargs)
        else:
            raise ValueError(f"'{function_name}' is not callable.")
    except KeyError:
        raise ValueError(f"Function '{function_name}' does not exist.")

######VALUES#########
