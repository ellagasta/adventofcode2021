import numpy as np
import re

with open('input.txt') as f:
	input = f.readlines()

input_fish = input[0].rstrip().split(',')
fish = {}
for entry in input_fish:
	if int(entry) not in fish.keys():
		fish[int(entry)] = 1
	else:
		fish[int(entry)] += 1


def day_step(fish):
	FISH_SPAWN_COOLDOWN = 6
	NEWFISH_COOLDOWN = 8
	new_fish = {}
	for i in range(NEWFISH_COOLDOWN+1):
		new_fish[i] = 0
	keys = fish.keys()
	keys.sort(reverse=True)
	for fish_age in keys: # oldest first
		if fish_age == 0:
			new_fish[FISH_SPAWN_COOLDOWN] += fish[fish_age]
			new_fish[NEWFISH_COOLDOWN] += fish[fish_age]
		else:
			new_fish[fish_age - 1] += fish[fish_age]
	print(new_fish)
	return new_fish

def q1(fish):
	for i in range(80):
		fish = day_step(fish)
	count = 0
	for timer in fish.keys():
		count += fish[timer]
	return count

def q2(fish):
	for i in range(256):
		fish = day_step(fish)
	count = 0
	for timer in fish.keys():
		count += fish[timer]
	return count



#print(q1(fish))
print(q2(fish))