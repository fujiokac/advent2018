import re
import sys
from itertools import chain

FILE = sys.argv[1]
REGEX = re.compile(r'(\d+)')

def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def parse_file(line):
	return iter([int(n) for n in line[0].split(' ')])

def parse_tree(license):
	n_children, n_metadata = next(license), next(license)
	children = [parse_tree(license) for n in range(n_children)]
	metadata = [next(license) for n in range(n_metadata)]
	return children, metadata

def sum_metadata(node):
	children, metadata = node
	return sum(metadata) + sum(sum_metadata(child) for child in children)

file = parse_file(read_file())
tree = parse_tree(file)
print(sum_metadata(tree))