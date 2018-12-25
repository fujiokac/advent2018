import re
import sys
import string
from collections import defaultdict, Counter
from itertools import chain

FILE = sys.argv[1]
WORKERS = int(sys.argv[2])
INTERVAL = int(sys.argv[3])
REGEX = re.compile(r' (\S) ')


def read_file():
	try:
		with open(FILE,'r') as file:
			return file.read().splitlines()
	finally:
		file.close()

def compile_instructions(lines):
	prereqs = defaultdict(set)
	for line in lines:
		prereq, step = REGEX.findall(line)
		prereqs[step].add(prereq)
		if prereq not in prereqs:
			prereqs[prereq] = set()
	return prereqs

def get_next_step(prereqs, todo, done):
	return min([step for step in todo if prereqs[step] <= done], default = None)

def time_per_step(step):
	return INTERVAL + 1 + string.ascii_uppercase.index(step)

def part1(prereqs):
	done = []
	todo = set(prereqs.keys())
	while(len(todo) > 0):
		step = get_next_step(prereqs, todo, set(done))
		done += step
		todo.discard(step)
	return ''.join(done)

def part2(prereqs):
	done = []
	todo = set(prereqs.keys())
	time = 0
	elves = {}
	while(True):
		# Check for completed tasks
		complete = [elf for elf in elves if elves[elf] <= time]
		for task in complete:
			elves.pop(task)
		done += complete
		todo -= set(complete)
		working_elves = len(elves)
		# End loop if all planned and ongoing tasks completed
		if(len(todo) == 0 and working_elves == 0):
			break
		# If any workers available, check for available work
		if working_elves < WORKERS:
			completed = set(done)
			# In case there is more work than workers
			for times in range(working_elves, WORKERS):
				step = get_next_step(prereqs, todo - set(elves.keys()), completed)
				if step is not None:
					# Add available work with time of completion
					elves[step] = time + time_per_step(step)
				else:
					# Nothing available right now
					break
		time += 1
	return ''.join(done), time

lines = read_file()
prereqs = compile_instructions(lines)
print(part1(prereqs))
print(part2(prereqs))