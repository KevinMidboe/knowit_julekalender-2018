#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-12-04 16:40:56
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-12-05 00:27:57

import re, os
from itertools import permutations

def get_wordlist():
	with open(os.path.dirname(__file__) + '/wordlist.txt', 'r') as wordlist:
		read_data = wordlist.read().splitlines()
	wordlist.close()
	return read_data

def get_letter_instances(word):
	letter_instances = {}
	for char in list(word):
		try:
			letter_instances[char] = letter_instances[char] + 1
		except KeyError:
			letter_instances.update({char: 1})

	return letter_instances

def bigram(word, n=2):
	gram = ''
	for i in range(len(word)):
		gram += word[i:i+n]
		if (len(word[i:i+n]) < n):
			gram = gram[:-len(word[i:i+n])]
	return ''.join(gram)

def anagrams(word):
	return [''.join(perm) for perm in permutations(word)]

def has_number(string):
	return bool(re.search(r'\d', string))

def main():
	anagramed_gram = 'aeteesasrsssstaesersrrsse'
	inst = get_letter_instances(anagramed_gram)
	keys = set(inst.keys())
	values = set(inst.values())
	wordlist = get_wordlist()

	for word in wordlist:
		if (has_number(word)): continue
		word = word.lower()
		# print('Working on word:', word)
		n = 1
		if set(get_letter_instances(word).keys()) == keys:
			while True:
				b = bigram(word, n)
				# print(b)

				if set(get_letter_instances(b).values()) == values:
					print('match', word, n)
					# exit(0)
					break

				if (n > len(anagramed_gram) or len(b) > len(anagramed_gram)):
					break
				n+=1
	exit(0)

	snowflake = bigram('snowflake', 2)
	mistletoe = bigram('mistletoe', 3)

	print([snowflake, mistletoe])
	# print(anagrams('snowflake'))

if __name__ == '__main__':
	main()
