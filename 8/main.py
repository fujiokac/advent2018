import sys

FILE = sys.argv[1]

def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def parse_file(line):
	return iter([int(n) for n in line[0].split(' ')])

def parse(license):
	n_children, n_metadata = next(license), next(license)
	children = [parse(license) for n in range(n_children)]
	metadata = [next(license) for n in range(n_metadata)]
	return children, metadata

def sum_metadata(node):
	children, metadata = node
	return sum(metadata) + sum(sum_metadata(child) for child in children)


def value_of(node):
	children, metadata = node
	if children:
		return sum(value_of(children[index-1]) for index in metadata if 1 <= index <= len(children))
	return sum(metadata)



file = parse_file(read_file())
node = parse(file)
print(sum_metadata(node))
print(value_of(node))