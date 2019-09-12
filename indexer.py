import index_file, folder_reader, sys, os, pickle, regex, math

def calc_tf(word, doc):
	amount = len(master_index[word][doc])
	return amount / wordcounts[doc]

def calc_idf(word):
	docs_n = len(files)
	#docswithword_n = 1
	docswithword_n = 0
	if master_index.__contains__(word):
		docswithword_n += len(master_index[word])
	return math.log10(docs_n / docswithword_n)

def calc_tfidf(word, doc):
	return calc_tf(word, doc)*calc_idf(word)

dir_path = "Selma/"
if len(sys.argv) > 1:
    dir_path = sys.argv[1]
if not dir_path.endswith("/"):
	dir_path += ("/")

files = folder_reader.get_files(dir_path, "txt")
wordcounts = {}

for file in files:
    wordcounts[file] = index_file.run(dir_path+file)

indexfiles = folder_reader.get_files(dir_path, "idx")
master_index = {}

for indexfile in indexfiles:
	index = pickle.load( open( dir_path+indexfile, "rb" ) )
	docname = regex.sub(".idx", ".txt", indexfile)
	for word in index:
		entry = {docname: index[word]}
		if master_index.__contains__(word):
			master_index[word][docname] = index[word]
		else:
			master_index[word] = entry

doc_tfidfs = {}
for master_word in master_index:
	master_entry = master_index[master_word]
	for doc in master_entry:
		if not doc_tfidfs.__contains__(doc):
			doc_tfidfs[doc] = {}
		doc_tfidfs[doc][master_word] = calc_tfidf(master_word, doc)

def calc_cos_sim(arr1, arr2):
	dot = sum(arr1[a]*arr2[b] for a, b in zip(arr1, arr2))
	#dot = sum([arr1[i] * arr2[i] for i in range(len(arr2))])
	mag1 = math.sqrt(sum(arr1[a]**2 for a in arr1))
	mag2 = math.sqrt(sum(arr2[b]**2 for b in arr2))
	cos = dot / (mag1 * mag2)
	return cos

cos_sim_matrix_set = {}
cos_sim_matrix = [[0 for i in range(len(files))] for j in range(len(files))]

i = 0
for doc1 in files:
	j = 0
	for doc2 in files:
		cos_sim_matrix_set[doc1] = {doc2: calc_cos_sim(doc_tfidfs[doc1], doc_tfidfs[doc2])}
		print(i,j)
		cos_sim_matrix[i][j] = cos_sim_matrix_set[doc1][doc2]
		j += 1
	i += 1

#	d1	d2	d3	d4
#d1	x 	12	13	14
#d2 21	x 	23	24
#d3	31	32	x 	34
#d4 41	42	43	x
#print(master_index["nils"]["jerusalem.txt"])
#print(doc_tfidfs["bannlyst.txt"]["et"])
#print(cos_sim_matrix_set)
#print(cos_sim_matrix)