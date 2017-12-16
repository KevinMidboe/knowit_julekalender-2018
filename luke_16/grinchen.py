#!/usr/bin/env python3.6
import os

def readFile():
    with open(os.path.dirname(__file__) + '/hjelpere.txt', 'r') as hjelpere:
        read_data = hjelpere.read().splitlines()
    hjelpere.close()
    return read_data

def main():
	entry_list = readFile()
	highest_value = []

	light_state = False
	memory = [False for i in range(100)]
	counter = 0
	for i, entry in enumerate(entry_list):
		entry = int(entry)-1
		if entry == 0 and light_state:
			counter += 1
			light_state = False
			if (counter >= 99):
				highest_value.append(i)
		else:
			if memory[entry] == False and light_state == False:
				memory[entry] = True
				light_state = True


	print(min(highest_value)+1)

if __name__ == '__main__':
    main()
