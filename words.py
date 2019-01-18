#!/usr/bin/env python3
# shebang is the absolute path to the Bash interpreter
import sys
from urllib.request import urlopen

# docs can be acces by help(function_name)
def fetch_words(url):
	"""Fetch a list of words from a URL.

	Args: url: the url of a text document 
	
	Returns: a list fo strings contained in the url text
	"""
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


def print_words(story_words):
	"""Print items one per line
	
	Args: a list / iterable series of items
	"""				
	for word in story_words:
		print(word)


def main(url):
	# url = sys.argv[1] -- will cause error
	words = fetch_words(url)
	print_words(words)


if __name__ == '__main__':
	main(sys.argv[1])