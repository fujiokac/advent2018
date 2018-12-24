import re
import sys
from collections import defaultdict

FILE = sys.argv[1]
REGEX = re.compile(r' (\S) ')

def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def compile_instructions(lines):
	steps = defaultdict(set)
	for line in lines:
		prereq, step = REGEX.findall(line)
		steps[step].add(prereq)
		if prereq not in steps:
			steps[prereq] = set()
	return steps

def step_order(steps):
	done = []
	not_done = set(steps.keys())
	while(len(not_done) > 0):
		step = min([step for step in not_done if steps[step] <= set(done)])
		done += step
		not_done.discard(step)
	return ''.join(done)

lines = read_file()
steps = compile_instructions(lines)
print(step_order(steps))