
# Using enumerate for roll_call_dwarves to avoid manual index management
def roll_call_dwarves(dwarf_list):
    for index, name in enumerate(dwarf_list, start=1):
        print(f'{index}. {name}')

# Using map and a lambda function for summon_captain_planet for a more functional approach
def summon_captain_planet(planeteer_calls):
    return list(map(lambda call: f'{call.title()}!', planeteer_calls))

# Using any() for long_planeteer_calls to simplify the logic
def long_planeteer_calls(words):
    return any(len(word) > 4 for word in words)
    # for i in range(len(words)):
        # if len(words[i] > 4):
    #     return True
    # return false

# Using next with a generator expression for find_the_cheese for a more concise approach
cheesez = ["camembert", "gouda", "cheddar"]

def find_the_cheese(foods):
    return next((food for food in foods if food in cheesez), None)

# words - any word length > 4 for word in words 