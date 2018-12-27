import sys
import re
from collections import deque
from itertools import cycle

FILE = sys.argv[1]
REGEX = re.compile(r'(\d+)')

def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def read_games(file):
	return [tuple(map(int,REGEX.findall(line))) for line in file]

def evaluate_game(game):
	n_players, last_marble = game
	players = [0] * n_players
	player = cycle(range(n_players))
	marbles = deque()
	for marble in range(last_marble+1):
		p = next(player)
		if marble % 23 == 0 and marble != 0:
			players[p] += marble
			marbles.rotate(-7)
			players[p] += marbles.pop()
		else:
			marbles.rotate(2)
			marbles.append(marble)
	return players

games = read_games(read_file())
for game in games:
	result = evaluate_game(game)
	print(max(result))