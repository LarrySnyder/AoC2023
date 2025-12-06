
#import numpy as np
import time
#import tqdm
#import functools
#import networkx as nx


DAY = 1
PART = 2
SAMPLE = False
if SAMPLE:
	if PART == 1:
		FILENAME = f'day{DAY}/aoc_day{DAY}_sample_input.txt'
	else:
		FILENAME = 'day1/aoc_day1_part2_sample_input.txt'
else:
	FILENAME = f'day{DAY}/aoc_day{DAY}_input.txt'

NUMERALS = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def read_data():
	with open(FILENAME) as f:
		data = f.read().splitlines() # splitlines gets rid of \n at end of lines
	return data

def is_number(line, index):
	if line[index].isdigit():
		return int(line[index])
	for n in range(1, 10):
		if index + len(NUMERALS[n]) <= len(line) and line[index:index+len(NUMERALS[n])] == NUMERALS[n]:
			return n
	return None

def solve_aoc():
	data = read_data()
	
	sum_cal_values = 0
	for line in data:
		if PART == 1:
			first_digit = next(a for a in line if a.isdigit())
			last_digit = next(z for z in line[::-1] if z.isdigit())
		else:
			for m in range(len(line)):
				n = is_number(line, m)
				if n:
					first_digit = n
					break
			for m in range(len(line) - 1, -1, -1):
				n = is_number(line, m)
				if n:
					last_digit = n
					break

		cal_val = 10 * first_digit + last_digit
		sum_cal_values += cal_val

		print(f'{line}: {cal_val}')

	result = sum_cal_values

	return result

if __name__ == "__main__":
    start_time = time.time()
    result = solve_aoc()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
