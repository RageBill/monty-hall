import random
from collections import defaultdict

NUMBER_OF_SIMULATIONS = 1000000

def monty_hall():
    # Starting the game
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    # Player randomly pick door
    player_choice = random.randint(0, 2)

    # Host reveals a goat behind one of the door
    doors_left = doors[:player_choice] + ['chosen'] + doors[player_choice+1:]
    goat_door_to_open = doors_left.index('goat')
    doors = doors[:goat_door_to_open] + ['goat (opened)'] + doors[goat_door_to_open+1:]

    # Player decides whether to choose another door
    change = random.choice([True, False])
    if change:
        if doors[player_choice] is 'goat':
            player_choice = doors.index('car')
        else:
            player_choice = doors.index('goat')
    return change, doors[player_choice]

changed = defaultdict(int)
not_changed = defaultdict(int)
for i in range(NUMBER_OF_SIMULATIONS):
    change, result = monty_hall()
    if change:
        changed[result] += 1
    else:
        not_changed[result] += 1
changed_times = changed['goat'] + changed['car']
changed_win_rate = changed['car']/(changed['goat'] + changed['car'])*100
not_changed_times = not_changed['goat'] + not_changed['car']
not_changed_win_rate = not_changed['car']/(not_changed['goat'] + not_changed['car'])*100
print(f'{NUMBER_OF_SIMULATIONS} simulations have been run.')
print(f'The player took {changed_times} times changing the choice, {not_changed_times} times not changing.')
print(f'Win rate for changing choice after reveal: {changed_win_rate:0.2f}%.')
print(f'Win rate for not changing choice after reveal: {not_changed_win_rate:0.2f}%.')
