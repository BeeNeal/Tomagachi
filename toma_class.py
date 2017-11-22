
class Tomagachi(object):

    def __init__(self, name):
        print "Congratulations! {} has entered the world ".format(name)
        self.name = name
        self.height = 1.0
        self.weight = 1.0
        self.hunger = 20
        self.temperament = "mild"

    def eat(self, food="grub"):
        """feeds toma - hunger decreases based on type/amount of food"""

        if food == "grub":
            self.hunger -= 1
        elif food == "pistachios":
            self.hunger -= 2
        elif food == "vindaloo":
            self.hunger -= 5
            print self.hunger
        elif food == self.favorite_food:
            print "Yummo!"
            self.hunger = 0
        return self.hunger


class HappyTomagachi(Tomagachi):
    """Happy Tomagachi"""

    motto = "Every day is the best day!"
    favorite_food = "pickles"


# name = raw_input("What's your Gachi's name?")

# # task: random int image





# Notes:
# getattr(object, 'attr-name', [default-value])
#   getattr(fido, 'tail_length', 'unknown')
#

# super(ThisClass, self).methodName(arguments)
# class Cat(Animal):

#     def __init__(self, name):
#         super(Cat, self).__init__(name, 'cat')
