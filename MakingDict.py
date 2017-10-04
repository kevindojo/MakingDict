name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(name, favorite_animal):
    for i in range(min(len(name), len(favorite_animal))):   #range needs a minimum, start, end
        print name[i],  ":" , favorite_animal[i]

make_dict(name,favorite_animal)