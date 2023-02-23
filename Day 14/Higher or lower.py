from game_data import data
import random

A = random.choice(data)
B = random.choice(data)
while B == A:
    B = random.choice(data)
print("Compare A: "+str(A["name"])+", a "+str(A["description"])+" from "+str(A["country"]))
print("Compare B: "+str(B["name"])+", a "+str(B["description"])+" from "+str(B["country"]))
