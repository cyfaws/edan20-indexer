import index_file, folder_reader, sys, os, pickle, regex

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = sys.argv[1]
if not dir_path.endswith("/"):
	dir_path += ("/")

files = folder_reader.get_files(dir_path, "txt")

for file in files:
    index_file.run(dir_path+file)

indexfiles = folder_reader.get_files(dir_path, "idx")
master_index = {}

for indexfile in indexfiles:
	index = pickle.load( open( dir_path+indexfile, "rb" ) )

	entryname = regex.sub(".idx", ".txt", indexfile)
	for word in index:
		entry = [{entryname: index[word]}]
		if master_index.__contains__(word):
			master_index[word].append(entry)
		else:
			master_index[word] = entry
print(master_index["samlar"])


#indices = []
#for indexfile in indexfiles:
#	indices.append( pickle.load( open( dir_path+indexfile, "rb" ) ))

#master_index = []
#for index in indices:
#	for word in index:
#		if master_index.__contains__(word) :
#		    print("")
#		else:
#		    master_index[word] = [index.replace(".txt", ""), index[word]]
#print(master_index)


