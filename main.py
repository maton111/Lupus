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

##################
### CLASS COMB ###
##################

class Comb:
    def __init__(self, guard, seer, seerbis, switcher, third, villager, vsupport, wolf, wsupport):
        self.guard = guard
        self.seer = seer
        self.seerbis = seerbis
        self.switcher = switcher
        self.third = third
        self.villager = villager
        self.vsupport = vsupport
        self.wolf = wolf
        self.wsupport = wsupport

    # def __str__(self):
    #     return(str(self.group)+": "+str(self.name))

    guard: int
    seer: int
    seerbis: int
    switcher: int
    third: int
    villager: int
    vsupport: int
    wolf: int
    wsupport: int

######################
### READ CARTE CSV ###
######################

def read_carte_csv(card):
    card_list = []
    with open(card, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            card_list.append(Carta(row["group"], row["name"], row["value"], row["priority"], row["constraint"]))
            line_count += 1
        return card_list

#####################
### READ COMB CSV ###
#####################

def read_comb_csv(comb_csv, giocatori):
    comb = Comb
    with open(comb_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if giocatori == int(row["nPlayers"]):
                if row["group"] == "guard":
                    comb.guard = row["nPg"]
                if row["group"] == "seer":
                    comb.seer = row["nPg"]
                if row["group"] == "seerbis":
                    comb.seerbis = row["nPg"]
                if row["group"] == "switcher":
                    comb.switcher = row["nPg"]
                if row["group"] == "third":
                    comb.third = row["nPg"]
                if row["group"] == "villager":
                    comb.villager = row["nPg"]
                if row["group"] == "vsupport":
                    comb.vsupport = row["nPg"]
                if row["group"] == "wolf":
                    comb.wolf = row["nPg"]
                if row["group"] == "wsupport":
                    comb.wsupport = row["nPg"]
            line_count += 1
        return comb

###################
### SCELTA COMB ###
###################

def get_comb(comb_random, comb_path, comb_perc):
    i = 0
    for comb in comb_path:
        if i == 0:
            if comb_random > 0 and comb_random <= int(comb_perc[i]):
                return comb
            i += 1
            continue

        if comb_random > int(comb_perc[i-1]) and comb_random <= int(comb_perc[i]):
            return comb

        i += 1

############
### MAIN ###
############

if __name__ == '__main__':
    # Chiamata a read_carte_csv
    card_list = read_carte_csv('carte.csv')

    # Scelta numero giocatori
    while True:
        giocatori = input("Inserisci il numero di giocatori: ")
        if giocatori != "":
            if int(giocatori) < 5:
                print(f"Solo {int(giocatori)}? Mettine più di 4")
            elif int(giocatori) > 30:
                print("Non ti sembrano un po' troppi?")
            else:
                break
        else:
            print("----------------------------------------")
            print("--- Inserisci un fottutissimo numero ---")
            print("----------------------------------------")

    giocatori = int(giocatori)

    # Scelta comb
    comb_random = random.randint(1, 100)
    comb_path = []
    comb_perc = []
    with open('comb_config.txt') as f:
        lines = f.read().split('\n')
        line_count = 0
        for row in lines:
            if 'csv' in row:
                comb_path.append(lines[line_count])
                comb_perc.append(lines[line_count+1])
            line_count += 1
    comb_name = get_comb(comb_random, comb_path, comb_perc)

    # Import CSV comb and put in class
    comb = read_comb_csv(comb_name, giocatori)

