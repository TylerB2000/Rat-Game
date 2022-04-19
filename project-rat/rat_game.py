#Game Idea: Monster Hunter(but not like that other one)

import random

#Set up Monster class
class Monster:
  def __init__(self, name, clan, level):
    self.name = name
    self.clan = clan
    self.level = level
    self.health = level * 2
    self.attack = int(round(level * 1.25, 0))
    self.is_dead = False
  
  #Monster representation line
  def __repr__(self):
    return 'You are facing a level {level} {name} from the {clan} clan. The {name} will deal {dmg} damage and has {health}HP left.'.format(level = self.level, clan = self.clan, name = self.name, dmg = self.attack, health = self.health)

  #What should happen when a monster dies
  def dead(self, player):
    #Set death to True so a new monster can spawn
    self.is_dead = True
    if self.health != 0:
      self.health = 0
    player.potions += 1
    #Give player a level for defeating Remy so they only will face one
    if self.name == 'Remy':
      player.exp += 100
    #Increased level progression for Skelly's so that first levels feel more rewarding  
    if self.name == 'Skelly':
        player.exp += (self.level * 20)
    #Decreased level progression for Ogre's because they are a higher default level
    if self.clan == 'Ogre':
      player.exp += (self.level * 2.5)
    #Default exp gain
    else:
      player.exp += (self.level * 5)
    print('{name} has been defeated! You have gained a potion and some XP!'.format(name = self.name))
    player.lvl_up()
    
  #What should happen when a monster takes damage
  def take_damage(self, amount, player):
    self.health -= amount
    #Determine if the damage was fatal
    if self.health <= 0:
      self.health = 0
      self.dead(player)
    else:
      print('{name} is down to {health}HP.'.format(name = self.name, health = self.health))

  #What should happen when a monster deals damage
  def deal_damage(self, player):
    dam = self.attack
    print('{name} attacked {player} for {damage} damage!'.format(name = self.name, player = player.name, damage = self.attack))
    player.take_damage(dam)

#Set up hero class
class Hero:
  def __init__(self, name, weapon, level, num_potions):
    self.name = name
    self.weapon = weapon
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.potions = num_potions
    self.attack = int(weapon[1])
    self.exp = 0
    self.is_dead = False

  #Hero representation line
  def __repr__(self):
    return 'Your hero {name} is level {lvl}, currently wields a {weapon}, and has {health}HP.'.format(name = self.name, lvl = self.level, weapon = self.weapon[0], health = self.health)
  
  #What should happen when the hero dies
  def dead(self):
    #Set lose condition to True if the hero dies
    self.is_dead = True
    if self.health != 0:
      self.health = 0
    print('Oh no! Your hero {name} has been defeated! Better luck next time!'.format(name = self.name))

  #What should happen when the hero levels up
  def lvl_up(self):
    if self.exp >= 100:
      self.level += 1
      #Carry over exp incase hero has more that 100 exp
      self.exp = self.exp - 100
      #Increase the hero's max health and restore their HP
      self.max_health = int(round(self.level * 3.5))
      self.health = self.max_health
      print('Congratulations, your hero is now level {level}! {name}\'s stats have increased and their health has been returned to full!'.format(level = self.level, name = self.name))
    print('Your hero now needs {exp} more XP to level up'.format(exp = 100 - self.exp))

  #What should happen when the hero takes damage
  def take_damage(self, amount):
    self.health -= amount
    #Determine if the damage was fatal
    if self.health <= 0:
      self.health = 0
      self.dead()
    else:
      print('{name} is now down to {health}HP.'.format(name = self.name, health = self.health))

  #What should happen when the hero uses the block action
  def block(self, mon):
    amount = int(round(mon.attack / 2))
    #Random number decides if player blocks attack
    roll = random.randint(1, 4)
    if roll == 1 or 2 or 3:
      self.health -= amount
      print('You have succesfully blocked the attack for {amount} damage. {name} is now down to {health}HP.'.format(amount = amount, name = self.name, health = self.health))
      #Monster rebound damage for succesfull block
      mon.take_damage(amount, self)
    else:
      print('You have failed to block the attack.')
      self.take_damage(amount)
  
  #What should happen when the hero deals damage
  def deal_damage(self, mon):
    dam = 0
    #Determines crit chance based on weapon
    if self.weapon == wep1:
      dam = self.attack * int(round(self.level))
      crit = random.randint(1, 3)
    elif self.weapon == wep2:
      dam = self.attack * int(round(self.level * .75))
      crit = random.randint(1, 5)
    elif self.weapon == wep3:
      dam = self.attack * int(round(self.level * .6))
      crit =  random.randint(1, 10)
    if crit == 1:
      print('Critical hit!')
      dam = dam * 2
    else:
      dam = dam
    print('{name} attacked {mon} for {damage} damage!'.format(name = self.name, mon = mon.name, damage = dam))
    mon.take_damage(dam, self)

  #What should happen when the hero uses a potion
  def use_potion(self):
    if self.potions > 0:
      self.health += 10
      #What should happen if healed health exceeds max health
      if self.health >= self.max_health:
        self.health = self.max_health
      print('{name} now has {health}HP'.format(name = self.name, health = self.health))
    else:
      print('You are out of potions :(')

#Weapon descriptions
wep1 = ['Dagger', 1]
wep2 = ['Sword', 2]
wep3 = ['Axe', 3]

#Get user inputs for the hero's name and what weapon to start with
name_input = input('Hello, and welcome to Monster Hunter(not that one)! What name would you like to give your hero? ')
choice = input('Which weapon would you like your hero to take on their journey? Type \'Dagger\'(1 damage, 30% crit chance), \'Sword\'(2 damage, 20% crit chance), or \'Axe\'(3 damage, 10% crit chance). ').title()
while choice != 'Dagger' and choice != 'Sword' and choice != 'Axe':
  choice = input('Whoops! Looks like that wasn\'t one of the choices! Please type \'Dagger\'(1 damage, 30% crit chance), \'Sword\'(2 damage, 20% crit chance), or \'Axe\'(3 damage, 10% crit chance). ').title()
if choice == 'Dagger':
  wep_choice = wep1
if choice == 'Sword':
  wep_choice = wep2
if choice == 'Axe':
  wep_choice = wep3

#Define the hero
hero = Hero(name_input, wep_choice, 1, 5)  

#Make sure first enemy is "Remy"
if hero.level == 1:
  mon = Monster('Remy', 'Rat', 1)

#Encounter reset default value
reset = True

#Encounter commands
while reset == True:
  #Get user input for encounter action
  if wep_choice == wep1:
    fight = input('{mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level)))).title()    
    while fight != 'Attack' and fight != 'Block' and fight != 'Heal':
      fight  = input('Invalid command, please try again. {mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level)))).title()
  if wep_choice == wep2:
    fight = input('{mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level * .75)))).title()
    while fight != 'Attack' and fight != 'Block' and fight != 'Heal':
      fight  = input('Invalid command, please try again. {mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level * .75)))).title()
  if wep_choice == wep3:
    fight = input('{mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level * .6)))).title()
    while fight != 'Attack' and fight != 'Block' and fight != 'Heal':
      fight  = input('Invalid command, please try again. {mon} {hero} What will you do? Type \'Attack\'(deal {dmg} damage), \'Block\'(75% chance to reflect half damage), or \'Heal\'(Heals 10HP: You have {pot} potions). '.format(mon = mon, hero = hero, pot = hero.potions, dmg = hero.attack * int(round(hero.level * .6)))).title()
  #Determine what should happen if the attack command is chosen
  if fight == 'Attack':
    reset = False
    #Monster buffer default value
    mon_attack = False
    hero.deal_damage(mon)
    if mon.is_dead == False and mon_attack == False:
      mon.deal_damage(hero)
      #Ensures that a dead monster doesn't attack the hero
      mon_attack = True
    #Win condition
    if mon.is_dead == True and mon.name == 'Big Cheese':
      print('WOW! YOU DID IT! YOU BEAT THE BIG CHEESE! YOU WIN!!!!!')
      break
    #Spawns a new enemy if the current one is dead
    while mon.is_dead == True:
      #Determines what enemy to spawn based on hero level
      if 1 < hero.level <= 3:
        m1Lvl = random.randint(2, 5)
        mon = Monster('Skelly', 'Skeleton', m1Lvl)
      if 3 < hero.level <= 5:
        m2Lvl = random.randint(6, 10)
        mon = Monster('Skully', 'Skeleton', m2Lvl)
      if 5 < hero.level <= 10:
        m3Lvl = random.randint(11, 20)
        mon = Monster('Grog', 'Ogre', m3Lvl)
      if 10 < hero.level <= 16:
        m4Lvl = random.randint(20, 30)
        mon = Monster('Greg', 'Ogre', m4Lvl)
      if hero.level > 16:
        mon = Monster('Big Cheese', 'Rat Mob', 35)
      #Resets monster death buffer so a new one can spawn  
      mon.is_dead == False
    #Lose condition sequence break
    if hero.is_dead == True:
      break
    #Encounter reset
    else:
      reset = True
  #Determine what should happen if the block command is chosen
  if fight == 'Block':
    reset = False
    hero.block(mon)
    #Win condition
    if mon.is_dead == True and mon.name == 'Big Cheese':
      print('WOW! YOU DID IT! YOU BEAT THE BIG CHEESE! YOU WIN!!!!!')
      break
    #Spawns a new enemy if the current one is dead
    while mon.is_dead == True:
      #Determines what enemy to spawn based on hero level
      if 1 < hero.level <= 3:
        m1Lvl = random.randint(2, 5)
        mon = Monster('Skelly', 'Skeleton', m1Lvl)
      if 3 < hero.level <= 5:
        m2Lvl = random.randint(6, 10)
        mon = Monster('Skully', 'Skeleton', m2Lvl)
      if 5 < hero.level <= 10:
        m3Lvl = random.randint(11, 20)
        mon = Monster('Grog', 'Ogre', m3Lvl)
      if 10 < hero.level <= 16:
        m4Lvl = random.randint(20, 30)
        mon = Monster('Greg', 'Ogre', m4Lvl)
      if hero.level > 16:
        mon = Monster('Big Cheese', 'Rat Mob', 35)
      #Resets monster death buffer so a new one can spawn  
      mon.is_dead == False
    #Lose condition sequence break
    if hero.is_dead == True:
      break
    #Encounter reset
    else:
      reset = True
  #Determine what should happen if the heal command is chosen
  if fight == 'Heal':
    reset = False
    hero.use_potion()
    #Encounter reset
    reset = True



