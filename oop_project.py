# This is just a beginner project 
from abc import ABC, abstractmethod

class item_needs(ABC):
    @abstractmethod
    def use(self, player):
        pass
    
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self._health = 100
        self.stats = {"strength": 1,
                      "level": 1}
        
    @property
    def health(self):
        return self._health
       
    @health.setter
    def health(self, value):
        if value > 100:
            self._health = 100
        elif value <= 0:
            self._health = 0
            print("player is dead")
        else:
            self._health = value
                
class Item:
    count = 0

    def __init__(self):
        Item.count += 1
        
    def display_count_items(self):
        print(f"You have this many items: {Item.count}")
        
class Potion(Item, item_needs):
    def __init__(self, healing_power, name):
        self.healing_power = healing_power 
        self.name = name 
        super().__init__()
    
    def __str__(self):
        return f"{self.name} {self.healing_power}"
    
    def use(self, player):
        print(f"the player healed his hp by {self.healing_power} points")
        player.health += self.healing_power
        player.inventory.remove(self)
        
        
class Weapon(Item, item_needs):
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name 
        super().__init__() 
        
    def __str__(self):
        return f"{self.damage} {self.name}"
           
    def use(self, player):
        print(f"The enemy lost {self.damage} hp")
        #possible lifesteal effect
        #possible enemy system
        
p = Player("Alex")

pot1 = Potion(20, "hp1")
pot2 = Potion(30, "hp2")
p.inventory.append(pot1)
p.inventory.append(pot2)
pot1.use(p)

