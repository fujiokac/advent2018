import re
import string
import sys
from collections import defaultdict, Counter

FILE = sys.argv[1]
REGEX = re.compile(r'\d+')

def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def parse_points(lines):
	points = {}
	for c, line in zip(string.ascii_letters, lines):
		x, y = map(int,REGEX.findall(line))
		points[c] = (x, y)
	return points

def find_bounds(points):
	xs, ys = zip(*points.values())
	return min(xs), max(xs), min(ys), max(ys)

def manhattan(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def find_closest(points, point):
	# Does not resolve correctly for ties
	# return min(points, key=lambda p: manhattan(point, p))
	distances = {p: manhattan(point, points[p]) for p in points}
	sorted_dist = sorted(distances.items(), key=lambda kv: kv[1])
	if sorted_dist[0][1] == sorted_dist[1][1]:
		return '.'
	else:
		return sorted_dist[0][0]

def make_map(points, func):
	dist_map = defaultdict(int)
	x1, x2, y1, y2 = find_bounds(points)
	for y in range(y1, y2+1):
		for x in range(x1, x2+1):
			dist_map[x,y] = func(points, (x,y))
	return dist_map

def print_map(pmap, xmax):
	# Just for testing
	for p in pmap:
		print(pmap[p], end='')
		if p[0] == xmax:
			print()

def part1_distances(points):
	distances = []
	x1, x2, y1, y2 = find_bounds(points)
	for y in range(y1, y2+1):
		for x in range(x1, x2+1):
			distances.append(find_closest(points, (x,y)))
	return Counter(distances)

def part_1():
	lines = sorted(read_file())
	points = parse_points(lines)
	print(part1_distances(points))
	# dist_map = make_map(points, find_closest)
	# print(Counter(dist_map.values()))

part_1()