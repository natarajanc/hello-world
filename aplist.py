import sys,re

s =sys.argv[1]
while (s.find("/./")>0) :
	s = s.replace("/./","/")
#print s

while ( len(s) > 0  and s.find("..") > 0) :
	s = re.sub(r"/?\w+/../?","",s)
	print s.find("..")

print s

