def attributs(content,simbols):
    ttrue=True
    cursors=0
    pos=0
    posactual=0
    posactual2=0
    posactual3=0
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
                    chars=simbol
        if pos>-1:
            if chars=="'" or chars=='"':
                posactual3=content.find('"',pos+1)
                posactual2=content.find("'",pos+1)
                if posactual3<0:
                    posactual3=posactual2
                if posactual2<0:
                    posactual2=posactual3
                if posactual3<posactual2:
                    posactual2=posactual3
                if posactual2>-1:
                    pos=posactual2
                    
            if 0==0:
                returnstring=content[cursors:pos].strip()
                if returnstring!="":
                    returnstring=returnstring.replace("|"," ")
                    returnlist=returnlist+[returnstring]
                cursors=pos+1
                if cursors>len(content)-1:
                    cursors=len(content)-1
                    ttrue=False 
        else:
             if cursors!=len(content)-1:
                 returnstring=content[cursors:].strip()
            
                 returnlist=returnlist+[returnstring]

             ttrue=False

    return returnlist
a='body href="https://www.w3schools.com" color="red" hello="hello world"' 
c=a[:]
l1=["|","'",'"']
a=c.replace(" ","|")
list1=attributs(a,l1)
for aa in list1:
    print(aa)