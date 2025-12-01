'''
Monster Arena
Author: Timo Roehle
Description: Funny little game
'''

import random
import sys

villains = [
    {'name': 'Kobold', 'hp': 30, 'atk': 5, 'crit': 15},
    {'name': 'Goblin', 'hp': 40, 'atk': 7, 'crit': 10},
    {'name': 'Orc', 'hp': 70, 'atk': 12, 'crit': 20},
]

class Fight_Round:
    def __init__(self, hero, villain):
        self._hero = hero
        self._villain = villain
        self._hero_action = ''
        self._villain_action = ''
    def read_user_input(self):
        print('[1] Angreifen')
        print('[2] Wegrennen')
        valid_choice = False
        while valid_choice == False:
            user_input = input('Deine Wahl? ')
            if user_input == '1':
                valid_choice = True
                self.calc_round(user_input)
            if user_input == '2':
                valid_choice = True

    def calc_round(self, user_action):
        #For now Heros Action allways comes first
        if user_action == '1':
            hero_attack = self._hero.attack()
            print(hero_attack)

class Fight:
    def __init__(self, hero, villain):
        self._hero = hero
        self._villain = villain
        self._rounds = [] # coming soon
        self._round_counter = 0
    def start_round(self):
        round = Fight_Round(self._hero, self._villain)
        round.read_user_input()
       
    def check_end_of_fight(self):
        if self._hero.check_death() or self._villain.check_death():
            return True
        return False
    def check_winner(self):
        if self._hero.check_death():
            return self._villain.get_name()
        if self._villain.check_death():
            return self._hero.get_name()
        return 'Fight is still ongoing'
    def info(self):
        print(f'Runde: {self._round_counter}: {self._hero.get_name()} gegen {self._villain.get_name()}')
    def conclusion(self):
        print(f'Winner: {self.check_winner()}')

class Arena:
    def __init__(self, hero):
        self._name = 'Monsterarena'
        self._hero = hero
        self._history = []
    def spawn_random_villain(self):
        index = random.randint(0, len(villains)-1)
        villain = Villain(
            villains[index]['name'],
            villains[index]['hp'],
            villains[index]['atk'],
        )
        return villain
    def fight_random(self):
        villain = self.spawn_random_villain()
        self.start_fight(villain)
    def start_fight(self, villain):
        fight = Fight(self._hero, villain)
        fight.start_round()

class Hero:
    def __init__(self, name):
        self._name = name
        self._hp = 100
        self._atk = 10
        self._crit = 25
        self._block = 10
    def get_name(self):
        return self._name
    def attack(self):
        attack_summary = {
            'strength': 'normal',
            'value': 0
        }
        dice = random.randint(1, 100)
        if dice > 70:
            attack_summary['strength'] = 'awsome'
            attack_summary['value'] = self.get_atk() * 2
        if dice < 30:
            attack_summary['strength'] = 'pathetic'
            attack_summary['value'] = self.get_atk() * 0.5
        return attack_summary
    def get_atk(self):
        # TODO check villain defense here
        return self._atk
    def get_hp(self):
        return self._hp
    def take_dmg(self, atk, crit):
        self._hp -= atk
    def check_death(self):
        if self._hp <= 0:
            return True
        return False
    
class Villain:
    def __init__(self, name, hp, atk):
        self._name = name
        self._hp = hp
        self._atk = atk
    def get_name(self):
        return self._name
    def get_atk(self):
        return self._atk
    def get_hp(self):
        return self._hp
    def take_dmg(self, atk):
        self._hp -= atk
        return self._hp
    def check_death(self):
        if self._hp <= 0:
            return True
        return False
    def attack(self):
        attack_summary: {
            'strength': 'normal',
            'value': 0
        }
        dice = random.randint(1, 100)
        if dice > 70:
            attack_summary['strength'] = 'awsome'
            attack_summary['value'] = self.get_atk() * 2
            return attack_summary
        if dice > 30:
            attack_summary['strength'] = 'normal'
            attack_summary['value'] = self.get_atk() * 1 
            return attack_summary
        attack_summary['strength'] = 'pathetic'
        attack_summary['value'] = self.get_atk() * 0.5
        return attack_summary
def eval_greeting_input():
    valid_choice = False
    while valid_choice == False:
        user_choice = input('Deine Wahl? ')
        if user_choice == '1':
            valid_choice = True
            user_name = read_user_name()
            start_game(user_name)
        if user_choice == '2':
            valid_choice = True
            sys.exit(0)

def read_user_name():
    print('Gib bitte deinen Namen ein, damit wir wissen, was wir auf deinen Grabstein schreiben sollen')
    player_name = input('Name: ')
    return player_name

def greeting():
    print('Willkommen zu Lotics Monster Arena')
    print('Besiege Monster, werde stärker, gewinne Preise')
    print('Bist du bereit dein Können unter Beweis zu stellen?')
    print('[1] Hey Ho Lets go!')
    print('[2] Ich hab vergessen meine braune Hose anzuziehen :(')

def start_game(name):
    hero = Hero(name)
    arena = Arena(hero)
    arena.fight_random()

greeting()
eval_greeting_input()
