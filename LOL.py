import random

champions = {"name" : "Jhin", 


class champion:
  def __init__(self, name, attack, defense, magicResist, 
               armor, health, cooldown, username):
    self.name = name;
    self.attack = attack;
    self.defense = defense;
    self.magicResist = magicResist;
    self.armor = armor;
    self.health = health;
    self.cooldown = cooldown;
    self.username = username;

  def attack(self):
    damage = random.randint(0, 100)
    return f"{self.name} has dealt {damage} damage"

  def heal(self):
    heal = random.randint(0, 100)
    self.health = self.health + heal

  def attacked(self, damage):
    self.health = self.health - damage
    

Gabi = champion("Jhin", 50, 50, 50, 50, 100, 10, "blackful")
Sorin = champion("Veigar", 10, 10, 10,10 , 100, 10, "sorinsejoaca")

print(f'{Gabi.health} \n')
Gabi.heal()
print(f'{Gabi.health} \n')
Gabi.attacked(100)
print(f'{Gabi.health} \n')
