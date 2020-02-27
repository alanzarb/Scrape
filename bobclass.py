# bob.py Class with Class variables


class BobClass:
    ''' population is a class variable '''

    population = 0

    def __init__(self, name):
        BobClass.population += 1

        print("Name:" + name)
        self.name = name

    def dupName(self):
        self.name = "{0} - {0}".format(self.name)
        print(self.name)

    def whoseName(self):
        return self.name

    def howMany(self):
        return self.population


if __name__ == "__main__":
    bb = BobClass("Fred")
    bb.dupName()
    print("whosename ->")
    nm = bb.whoseName()
    print(nm)
    bb = BobClass("george")
    bb = BobClass("Sam")
    bc = BobClass("Zak")
    print(bb.howMany())
    counter = bb.howMany()
    print("Population is {0}".format(counter))
