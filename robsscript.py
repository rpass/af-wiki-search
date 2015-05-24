path = "/Users/rob/dev/IR/newdocs"
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.contains('Beeld~'): 
            list_of_files[filename] = os.sep.join([dirpath, filename])

for a in list_of_files:
	print(a)