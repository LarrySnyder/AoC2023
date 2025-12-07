
#import numpy as np
import time
#import tqdm
#import functools
#import networkx as nx

DAY = 3
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

	# Identify part numbers.
	sum_of_part_nums = 0
	part_num_grid = [[None] * len(data[0]) for _ in range(len(data))]
	for l, line in enumerate(data):
		line_ptr = 0
		while True:
			digit_idces = [i for i, ch in enumerate(line) if ch.isdigit() and i >= line_ptr]
			if digit_idces == []:
				break

			# Find numbers.
			start_idx = min(digit_idces)
			j = start_idx + 1
			while j < len(line) and line[j].isdigit():
				j += 1
			end_idx = j - 1
			num = int(line[start_idx:end_idx+1])
			line_ptr = end_idx + 1

			# Check for adjacent symbol.
			is_part_num = False
			rows = range(max(0, l-1), min(len(data)-1, l+1) + 1)
			cols = range(max(0, start_idx-1), min(len(line)-1, end_idx+1) + 1)
			for r in rows:
				for c in cols: 
					if data[r][c] != '.' and not data[r][c].isdigit():
						# it's a symbol
						is_part_num = True
						break
				if is_part_num:
					break
			
			if is_part_num:
				sum_of_part_nums += num
				for c in range(start_idx, end_idx+1):
					part_num_grid[l][c] = num

	# # Initialize dict of part numbers adjacent to each *.
	# adj_parts = {(r, c): [] for r in range(len(data)) for c in range(len(data[0])) if data[r][c] == '*'}
	# for (r, c) in adj_parts:
	# 	# Check for adjacent part num.
	# 	rows = range(max(0, r-1), min(len(data)-1, r+1) + 1)
	# 	cols = range(max(0, c-1), min(len(data[0])-1, c+1), + 1)
	# 	for rr in rows:
	# 		for cc in cols:
	# 			if part_num_grid[rr][cc] is not None:
	# 				adj_parts[(r, c)].append(part_num_grid[rr][cc])
	# 				break # allow duplicate part # on another row but not this one

	# # Identify gears.
	# sum_of_gear_ratios = 0
	# gears = []
	# for g in adj_parts:
	# 	if len(adj_parts[g]) == 2:
	# 		gears.append(g)
	# 		gear_ratio = adj_parts[g][0] * adj_parts[g][1]
	# 		sum_of_gear_ratios += gear_ratio


	sum_of_gear_ratios = 0
	gears = []
	for l, line in enumerate(data):
		for ch, the_char in enumerate(line):
			if the_char == '*':
				adj_parts = set()
				rows = range(max(0, l-1), min(len(data)-1, l+1) + 1)
				cols = range(max(0, ch-1), min(len(line)-1, ch+1) + 1)
				for r in rows:
					for c in cols:
						if part_num_grid[r][c] is not None:
							adj_parts.add((part_num_grid[r][c], r)) # store row number to allow same part in multiple rows to be unique

				adj_parts = [part[0] for part in adj_parts]
				if len(adj_parts) == 2:
					# it's a gear
					adj_parts = list(adj_parts)
					gear_ratio = adj_parts[0] * adj_parts[1]
					sum_of_gear_ratios += gear_ratio
					gears.append((l, ch))

	result = sum_of_part_nums, sum_of_gear_ratios

	return result

if __name__ == "__main__":
    start_time = time.time()
    result = solve_aoc()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
