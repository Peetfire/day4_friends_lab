

#1
def get_name(person):
    return person["name"]
# 2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]
#3
def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    if food in snacks:
        return True
    return False
#4
def add_friend(person, friend):
    person["friends"].append(friend)

#5
def remove_friend(person, friend):
    person["friends"].pop(person["friends"].index(friend))

#6
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

# 9
def find_no_friends(persons):
    no_friends = []
    for person in persons:
        if len(person["friends"]) == 0:
            no_friends.append(person)
    return no_friends

# 10
def unique_favourite_tv_shows(persons):
    all_tv_shows = []
    for person in persons:
        if person["favourites"]["tv_show"] not in all_tv_shows:
            all_tv_shows.append(person["favourites"]["tv_show"])
    return all_tv_shows