import sys, regex, pickle

#test_string = "Geeksforgeeks,    is best @# Computer Science Portal.!!!"
#print("The original string is : " + test_string)
#res = regex.findall(r'\w+', test_string)
#res = regex.findall(r'\p{Word}+', test_string)
#print("The list of words is : " + str(res))
def run(inputfile):
#inputfile = sys.argv[1]
#outputfile = sys.argv[2].replace("txt", "idx")
	outputfile = inputfile.replace(".txt", ".idx")
	dictionary = {}
	#file = open(inputfile, "r")
	file = open(inputfile, "r")
	text = file.read()
	#text =  "Geeksforgeeks,    is best @# Computer Science Portal.!!!  is"

	matches = regex.finditer(r'\p{L}+', text)
	for match in matches:
		word = match.group().lower()
		if dictionary.__contains__(word) :
		    dictionary[word].append(match.start())
		else:
		    dictionary[word] = [match.start()]

	#print(dictionary)

	outfile = open(outputfile, 'wb')
	pickle.dump(dictionary, outfile)

if __name__ == "__main__":
   run(sys.argv[1])
