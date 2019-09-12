import sys, regex, pickle

def run(inputfile):
	outputfile = inputfile.replace(".txt", ".idx")
	dictionary = {}
	file = open(inputfile, "r", encoding='UTF-8')
	text = file.read().lower()

	wordcount = 0
	matches = regex.finditer(r'\p{L}+', text)
	for match in matches:

		word = match.group()
		pos = match.start()
		wordcount += 1

		if dictionary.__contains__(word) :
		    dictionary[word].append(pos)
		else:
		    dictionary[word] = [pos]

	outfile = open(outputfile, 'wb')
	pickle.dump(dictionary, outfile)
	return wordcount

if __name__ == "__main__":
   run(sys.argv[1])
