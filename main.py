# This Python script generate random composition of a player.

import csv
import random
from itertools import combinations

###################
### CLASS CARTE ###
###################

class Carta:
    def __init__(self, group, name, value, priority, constraint):
        self.group = group
        self.name = name
        self.value = value
        self.priority = priority
        self.constraint = constraint

    def __str__(self):
        return(str(self.group)+"."+str(self.name))

    group: str
    name: str
    value: int
    priority: int
    constraint: str
    desc: str

################
### READ CSV ###
################

def read_csv(carte):
    card_list = []
    with open(carte, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            card_list.append(Carta(row["group"], row["name"], row["value"], row["priority"], row["constraint"]))
            line_count += 1
        return card_list

############
### MAIN ###
############

if __name__ == '__main__':
    card_list = read_csv('carte.csv')
    print(card_list)
