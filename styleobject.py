
def tagse(content,start,end):
    starts=-1
    ends=-1
    ttrue=True
    index=0
    stringout=""
    for n in start:
        i=content.find(n)
        if i>-1:
            starts=i+len(n)+1
    for n in end:
        i=content.find(n)
        if i>-1:
            ends=i
    if starts>-1 and ends>-1:
        stringout=content[starts:ends]
    return stringout
files=input("give me a .html file? ")
f1=open(files,"r")
contents=f1.read()
f1.close()
tags=["<title","<TITLE"]
tage=["</title","</TITLE"]
print(tagse(contents,tags,tage))
tags=["<style","<STYLE"]
tage=["</style","</STYLE"]
contents=tagse(contents,tags,tage).replace("\n","").replace("\r","")
objs=contents.split("}")
for n in objs:
    nn=n.split("{")
    index=0
    for nnn in nn:
        nnn=nnn.strip()
        if index==0 and nnn!="":
            print(nnn+"=",end="")
        else:
            if nnn!="":
                print(nnn)
        index+=1
