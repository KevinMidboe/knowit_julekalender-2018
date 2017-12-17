#!/usr/bin/env python3.6
import subprocess, os

def main():
	path = os.path.dirname(os.path.realpath(__file__)) + '/bilde.png' 
	result = subprocess.run(['zsteg', path], stdout=subprocess.PIPE)
	decode = result.stdout.decode('utf-8')

	return decode

if __name__ == '__main__':
	main()