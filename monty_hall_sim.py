import random

n_sim = 100000


def monty_hill_problem(switch = False):
  doors = range(3)
  prize_door_idx = random.randint(0,2)

  participant_selection = random.randint(0,2)

  if switch:
    remaining_doors = [idx for idx, door in enumerate(doors) if idx != prize_door_idx and idx != participant_selection]
    remove_door_idx = remaining_doors[0] if len(remaining_doors) > 1 else random.choice(remaining_doors)

    switch_idx = [idx for idx, door in enumerate(doors) if idx != participant_selection and idx != remove_door_idx]

    participant_selection = switch_idx[0]


  result = 'win' if participant_selection == prize_door_idx else 'lose'

  return result

wins_stay = 0
wins_switch = 0

for n in range(n_sim):
  stay_result = monty_hill_problem()
  switch_result = monty_hill_problem(switch=True)

  if stay_result == 'win':
    wins_stay += 1

  if switch_result == 'win':
    wins_switch += 1

print('Win Percentange of participants who stay: ', (wins_stay/n_sim)*100,'%')
print('Win Percentange of participants who switch: ', (wins_switch/n_sim)*100,'%')
