#%%
import numpy as np
import matplotlib.pyplot as plt 

#%% 1.1

def greet(string):
    return "Hello, " + string + "!"

greet('Jenny')
# %%

def gridlocks(length):

    if length>=140 and length<=150:
        return 'Just right'

    elif length<=140:
        return 'Too short'

    elif length>=150:
        return 'Too wide'

gridlocks(160)

#%%

def square_list(list):

    return [x**2 for x in list]

square_list([1,2,3,4,5])
    

    




# %%
