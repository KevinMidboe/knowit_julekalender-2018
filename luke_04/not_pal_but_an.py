#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-12-04 16:40:56
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-12-16 14:09:31
import os

def get_wordlist():
	with open(os.path.dirname(__file__) + '/ordliste.txt', 'r') as wordlist:
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

def can_be_palindrom(word):
	instance = get_letter_instances(word)
	values = list(instance.values())
	odd = 0
	for value in values:
		if (value & 1):
			odd += 1

	return (odd <= 1)

def is_palindrom(string):
	return string == string[::-1]

def main():
	matches = []
	wordlist = get_wordlist()

	for word in wordlist:
		if (not is_palindrom(word) and can_be_palindrom(word)):
			matches.append(word)
			
	print(matches, len(matches))
	return len(matches)

if __name__ == '__main__':
	main()
