
#import numpy as np
import time
#import tqdm
#import functools
#import networkx as nx


DAY = 2
PART = 2
SAMPLE = False
if SAMPLE:
	FILENAME = f'day{DAY}/aoc_day{DAY}_sample_input.txt'
else:
	FILENAME = f'day{DAY}/aoc_day{DAY}_input.txt'

BAG = {'red': 12, 'green': 13, 'blue': 14}

def read_data():
	with open(FILENAME) as f:
		data = f.read().splitlines() # splitlines gets rid of \n at end of lines
	return data

def solve_aoc():
	data = read_data()
	
	games = []
	for line in data:
		sets_str = line.split(': ')[1].split('; ')
		game = []
		for s in sets_str:
			cubes_str = s.split(', ')
			cubes = {'blue': 0, 'red': 0, 'green': 0}
			for cube_str in cubes_str:
				if 'blue' in cube_str:
					cubes['blue'] = int(cube_str.split(' ')[0])
				if 'red' in cube_str:
					cubes['red'] = int(cube_str.split(' ')[0])
				if 'green' in cube_str:
					cubes['green'] = int(cube_str.split(' ')[0])
			game.append(cubes)
		games.append(game)

	if PART == 1:
		sum_of_possible = 0
		for g, game in enumerate(games):
			possible = True
			for cubes in game:
				if cubes['blue'] > BAG['blue'] or cubes['red'] > BAG['red'] or cubes['green'] > BAG['green']:
					possible = False
					break
			if possible:
				sum_of_possible += g + 1

		result = sum_of_possible
	else:
		sum_of_powers = 0
		for game in games:
			max_blue = max([cubes['blue'] for cubes in game])
			max_red = max([cubes['red'] for cubes in game])
			max_green = max([cubes['green'] for cubes in game])
			power = max_blue * max_red * max_green
			sum_of_powers += power
		
		result = sum_of_powers

	return result

if __name__ == "__main__":
    start_time = time.time()
    result = solve_aoc()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
