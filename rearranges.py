
import sys
import os


path = "D:/UserFolders/Letöltések"
#path = sys.argv[1]

entries = os.listdir(path)

files = []
for e in entries:
	path_ = os.path.join(path,e)
	if os.path.isfile(path_):
		files.append(e)

groups = {}

for f in files:
	_,ext = os.path.splitext(f)
	if ext in groups.keys():
		groups[ext].append(f)
	else:
		groups[ext] = [f]


file = open("./renames.log",'a',encoding="utf-8")
for i,k in enumerate(groups):
	print(k[1:])
	dir_path = os.path.join(path,k[1:])
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	
	
	for f in groups[k]:
		print("		",f)
		try:
			src = os.path.join(path,f)
			dst = os.path.join(dir_path,f)
			os.rename(src,dst)
			file.write("{};{}\n".format(src,dst))
		except FileExistsError as e:
			print(e)
file.close()





