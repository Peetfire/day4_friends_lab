

#1
def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    if snacks.index(food) != ValueError:
        return True
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].pop(person["friends"].index(friend))

def total_money(persons):
    total = 0
    for person in persons:
        total += person["monies"]
    return total

# 7
def add_money(person, amount):
    person["monies"] = person["monies"] + amount
        
def sub_money(person, amount):
    person["monies"] = person["monies"] - amount

def lend_money(person_1, person_2, amount):
    sub_money(person_1, amount)
    add_money(person_2, amount)

# 8
def get_foods(person):
    return person["favourites"]["snacks"]

def all_favourite_foods(persons):
    favourite_foods = []
    for person in persons:
        foods = get_foods(person)
        for food in foods:
            favourite_foods.append(food)
    return favourite_foods
