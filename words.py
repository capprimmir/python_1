# refactor code to have a function and add __name__ to be able to execute 
# as script directly from REPL
from urllib.request import urlopen

def fecth_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
				
	for word in story_words:
		print(word)

# _ _ name _ _ detects if modules is runing as script or imported into another module
if __name__ == '__main__':
	fecth_words()