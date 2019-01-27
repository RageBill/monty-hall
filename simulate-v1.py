import random

# Starting the game
doors = ['car', 'goat', 'goat']
random.shuffle(doors)
results = ', '.join(doors)
print('Items behind the doors:')
for i, door in enumerate(doors):
    print(f'Door {i}: {door}')

# Player randomly pick door
player_choice = random.randint(0, 2)
print(f'User picked door {player_choice} ({doors[player_choice]}).')

# Host reveals a goat behind one of the door
doors_left = doors[:player_choice] + ['chosen'] + doors[player_choice+1:]
goat_door_to_open = doors_left.index('goat')
doors = doors[:goat_door_to_open] + ['goat (opened)'] + doors[goat_door_to_open+1:]
print(f'The host has opened door {goat_door_to_open} and reveals the goat.')

# Player decides whether to choose another door
change = random.choice([True, False])
print(f'The player {"changes" if change else "does not change"} the choice.')
if change:
    if doors[player_choice] is 'goat':
        player_choice = doors.index('car')
    else:
        player_choice = doors.index('goat')
print(f'The player opens door {player_choice} and reveals the {doors[player_choice]} as the prize.')