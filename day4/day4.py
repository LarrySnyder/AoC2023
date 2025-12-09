
import numpy as np
import time
#import tqdm
#import functools
#import networkx as nx


DAY = 4
PART = 2
SAMPLE = False
if SAMPLE:
	FILENAME = f'day{DAY}/aoc_day{DAY}_sample_input.txt'
else:
	FILENAME = f'day{DAY}/aoc_day{DAY}_input.txt'

RIGHT = np.array((0, 1))
LEFT = np.array((0, -1))
UP = np.array((-1, 0))
DOWN = np.array((1, 0))

def read_data():
	with open(FILENAME) as f:
		data = f.read().splitlines() # splitlines gets rid of \n at end of lines
	return data

def count_winners(winner_row, ticket_row):
	num_winners = 0
	for n in winner_row:
		if n in ticket_row:
			num_winners += 1
	return num_winners

def part1(winners, tickets):

	total_points = 0
	for r, winner_row in enumerate(winners):
		points = None
		for n in winner_row:
			if n in tickets[r]:
				if points is None:
					points = 1
				else:
					points *= 2
		total_points += points or 0 

	result = total_points
	return result

def part2(winners, tickets):

	num_tickets = len(winners)

	# First count winners on each card.
	# NB: cards are 1-indexed
	num_winners = {r: count_winners(winners[r-1], tickets[r-1]) for r in range(1, num_tickets + 1)}

	total_cards = len(winners)
	active_cards = list(range(1, len(winners) + 1))
	while len(active_cards) > 0:
		card_num = active_cards.pop()
		if card_num < num_tickets:
			cards_to_add = list(range(card_num + 1, min(card_num + num_winners[card_num], num_tickets) + 1))
			active_cards += cards_to_add
			total_cards += len(cards_to_add)
		
	result = total_cards

	return result
		
def solve_aoc():
	data = read_data()

	card_strs = [row.split(': ') for row in data]
	split_strs = [row[1].split(' | ') for row in card_strs]
	winner_strs = [row[0] for row in split_strs]
	ticket_strs = [row[1] for row in split_strs]
	winners = [tuple(int(n) for n in row.split()) for row in winner_strs]
	tickets = [tuple(int(n) for n in row.split()) for row in ticket_strs]

	if PART == 1:
		result = part1(winners, tickets)
	else:
		result = part2(winners, tickets)

	return result

if __name__ == "__main__":
    start_time = time.time()
    result = solve_aoc()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
