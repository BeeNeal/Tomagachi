
images = ["http://www.doglib.com/wp-content/uploads/dw/dwarf-smallest-breeds-of-cats.jpg",
          "https://i.pinimg.com/736x/e4/45/2c/e4452cc8ef5d6dac58d8b0b0aa290ac8--adorable-kittens-cute-kitty.jpg",
          "https://i.pinimg.com/736x/23/94/6b/23946be92b6c0d0da21bf4f9ec0fa637--mystique-animal-pictures.jpg",
          "https://i.pinimg.com/736x/13/b8/e6/13b8e6b21836fd797fbc6baeb6c24a7c--cat-fishing-cute-tigers.jpg",
          "http://slappedham.com/wp-content/uploads/2014/06/Cute-fluffy-dog.jpg"]


class Tomagachi(object):

    def __init__(self, name):
        print "Congratulations! {} has entered the world ".format(name)
        self.name = name
        self.height = 1.0
        self.weight = 1.0
        self.hunger = 20
        self.temperament = "mild"
        self.image = images.pop()


    def eat(self, food="grub"):
        """feeds toma - hunger decreases based on type/amount of food"""

        if food == "grub":
            self.hunger -= 1
        elif food == "pistachios":
            self.hunger -= 2
        elif food == "vindaloo":
            self.hunger -= 5
        elif food == self.favorite_food:
            self.hunger = 0
        else:
            self.hunger += 1
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
