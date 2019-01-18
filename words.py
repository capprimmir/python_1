import sys
from urllib.request import urlopen

def fetch_words(url):
	# 'http://sixty-north.com/c/t.txt'
	# change to accept an url instead of passing the string
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words
				
def print_words(story_words):				
	for word in story_words:
		print(word)

def main(url):
	# url = sys.argv[1] -- will cause error
	words = fetch_words(url)
	print_words(words)


if __name__ == '__main__':
	main(sys.argv[1])