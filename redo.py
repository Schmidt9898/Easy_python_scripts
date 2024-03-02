
import sys
import os

path = "./renames.log"

file = open(path,'r',encoding="utf-8")
lines = file.readlines()
file.close()

changes = [tuple(l.strip().split(';')) for l in lines]

for c in changes:
	print(c)
	try:
		dst,src = c
		os.rename(src,dst)
	except Exception as e:
		print(e)






