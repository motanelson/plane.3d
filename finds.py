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
        pos=cursors
        
        for simbol in simbols:
            posactual=content.find(simbol,cursors)
            
            if posactual!=-1 and posactual>=cursors:
                
                if posactual<pos or pos==cursors:
                    
                    pos=posactual
        if pos>cursors:
            returnstring=content[cursors:pos]
            returnlist=returnlist+[returnstring]
            cursors=pos+1
            if cursors>len(content)-1:
                cursors=len(content)-1 
        else:
            ttrue=False

    return returnlist
a='body href="https://www.w3schools.com" color="red"' 
c=a[:]
l1=["|","'",'"']
a=c.replace(" ","|")
print(attributs(a,l1))