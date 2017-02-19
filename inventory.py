class Item:
    def __init__(self):

        self.name = ''
        self.weight = 0
        self.value = 0

class Weapon(Item):
    def __init__(self):

        self.type = '' #eg simple, martial, ranged
        self.die = '' # eg 2d6 + 3
        self.mod = '' #ranged, versatile, etc

class Armour(Item):
    def __init__(self):

        self.AC = 0
        self.type = '' #eg light armour, medium armour, heavy armour

class Other(Item):
    def __init__(self):

        self.desc = '' #just put all yo sheet here

class Inventory:
    def __init__(self):

        self.contents = ()
