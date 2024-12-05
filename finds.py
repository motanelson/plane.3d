def attributs(content,simbols):
    ttrue=True
    cursors=0
    pos=0
    posactual=0
    returnlist=[]
    chars=""
    returnstring=""
    while ttrue:
        chars=""
        posactual=-1
        pos=-1
        
        for simbol in simbols:
            posactual=content.find(simbol,cursors)
            
            if posactual!=-1:
                
                if posactual<pos or pos==-1:
                    pos=posactual
        if pos>-1:
            returnstring=content[cursors:pos].strip()
            if returnstring!="":
                returnlist=returnlist+[returnstring]
            cursors=pos+1
            if cursors>len(content)-1:
                cursors=len(content)-1
                ttrue=False 
        else:
            ttrue=False

    return returnlist
a='body href="https://www.w3schools.com" color="red"' 
c=a[:]
l1=["|","'",'"']
a=c.replace(" ","|")
list1=attributs(a,l1)
for aa in list1:
    print(aa)