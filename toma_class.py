
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


name = raw_input("What's your Gachi's name?")

# task: try to make an instance tied to the user input




zink = HappyTomagachi("Zink")
gachi = raw_input("which Gachi's yours? ").lower()
food_choice = raw_input("what do you want to feed your gachi ")
if gachi == 'zink':
    zink.eat(food_choice)

#this doesn't work because gachi is a string here, so doesn't act as instance
# will have same problem with HTML

# problem - raw input to have user feed - would be better to have dropdown set of options
# let's knock out the raw input tonight, start on the html tomorrow!


# Problem: favorite_food of an instance not linking to subclass's favorite_food
# solution: use self in parent


# IDEAS:
    # Can I set a favorite food per instance, then if eat("favorite food") subtract more hunger?



# Notes:
# getattr(object, 'attr-name', [default-value])
#   getattr(fido, 'tail_length', 'unknown')
#

# super(ThisClass, self).methodName(arguments)
# class Cat(Animal):

#     def __init__(self, name):
#         super(Cat, self).__init__(name, 'cat')