

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
        