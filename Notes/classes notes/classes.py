#Alex Anderson, Classes Notes


# What is a class in python?
# A blueprint for creating an object

# What is an object in python?
# A specific instance of a class

# How do python classes relate to python objects?
# object are defined inside of classes

# How do you create a python class?
# class name:

# What are methods?
# A function that is specific to a class

# How do you create a python object?
# def name(paramiters)

# How to you call a method for an object?
# object.method(paramiter)

# Why do we use python classes
# orginizes info better, is more convieniant, simplifies later code


# Example Code:

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg
    
    def __str__(self):
        return f'Name: {self.name}\nSpecies:{self.species}\nHp:{self.hp}\nDmg:{self.dmg}'

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp} health!')
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp} health!')
                if self.hp <= 0:
                    print(f'{self.name} has been killed. {opponent.name} won the battle!')
            else:
                print(f'{opponent.name} has been killed. {self.name} won the battle!')
            

dracula = pokemon("Mr.Dracula","Charizard",99,1)
salid = pokemon("Salid","Bulbasaur",100,1)

print(salid)
dracula.battle(salid)
