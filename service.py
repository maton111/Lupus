# Import del file config
import configparser
import random

config = configparser.ConfigParser()
config.read("config.ini")

###################
### UPDATE CARD ###
###################
def update_card(card_list):
    config["Cards"] = {'TotalCard': 0,
                       'GuardCard': 0,
                       'SeerCard': 0,
                       'SeerbisCard': 0,
                       'SwitcherCard': 0,
                       'ThirdCard': 0,
                       'VillagerCard': 0,
                       'VsupportCard': 0,
                       'WolfCard': 0,
                       'WsupportCard': 0}

    for card in card_list:
        config["Cards"]["TotalCard"] += "0"
        if card.group == "guard":
            config["Cards"]["GuardCard"] += "0"
        if card.group == "seer":
            config["Cards"]["SeerCard"] += "0"
        if card.group == "seerbis":
            config["Cards"]["SeerbisCard"] += "0"
        if card.group == "switcher":
            config["Cards"]["SwitcherCard"] += "0"
        if card.group == "third":
            config["Cards"]["ThirdCard"] += "0"
        if card.group == "villager":
            config["Cards"]["VillagerCard"] += "0"
        if card.group == "vsupport":
            config["Cards"]["VsupportCard"] += "0"
        if card.group == "wolf":
            config["Cards"]["WolfCard"] += "0"
        if card.group == "wsupport":
            config["Cards"]["WsupportCard"] += "0"
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    config["Cards"]["TotalCard"] = str(len(config["Cards"]["TotalCard"]) - 1)
    config["Cards"]["GuardCard"] = str(len(config["Cards"]["GuardCard"]) - 1)
    config["Cards"]["SeerCard"] = str(len(config["Cards"]["SeerCard"]) - 1)
    config["Cards"]["SeerbisCard"] = str(len(config["Cards"]["SeerbisCard"]) - 1)
    config["Cards"]["SwitcherCard"] = str(len(config["Cards"]["SwitcherCard"]) - 1)
    config["Cards"]["ThirdCard"] = str(len(config["Cards"]["ThirdCard"]) - 1)
    config["Cards"]["VillagerCard"] = str(len(config["Cards"]["VillagerCard"]) - 1)
    config["Cards"]["VsupportCard"] = str(len(config["Cards"]["VsupportCard"]) - 1)
    config["Cards"]["WolfCard"] = str(len(config["Cards"]["WolfCard"]) - 1)
    config["Cards"]["WsupportCard"] = str(len(config["Cards"]["WsupportCard"]) - 1)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

##############################
### RANDOM AND CHECK VALUE ###
##############################
def random_and_check(value, card):
    random_list = []
    if int(value) > 0:
        i = 0
        while i != int(value):
            random_list.append(random.randint(0, int(config["Cards"][card]) - 1))
            if len(random_list) > 1:
                random_list = list(set(random_list))
            i = len(random_list)
    return random_list