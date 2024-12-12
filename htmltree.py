
class nodes:
    def __init__(self,value):
        self.value=value
        self.nexts=None
        self.childs=None

    def report(self):
        stack=[]
        ttrue=True
        back=self
        
        while ttrue:
            
            if back!=None:
                
                print("    "*len(stack)+back.value)
                if back.childs!=None:
                    stack=stack+[back]
                    back=back.childs
                else:
                    if back.nexts!=None:
                        back=back.nexts
                    else:
                        if len(stack)>0:
                            back=stack.pop()
                            back=back.nexts
                        else:
                            ttrue=False
                            
            else:
                ttrue=False
            
           



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
    ons=0
    
    while ttrue:
        chars=""
        posactual=-1
        pos=-1
        for simbol in simbols:
            posactual=content.find(simbol,ons)
            if posactual!=-1:
                if posactual<=pos or pos==-1:
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
                    pos=posactual2+1
                    ons=pos
                    
            
            
            if chars==simbols[0]:
                returnstring=content[cursors:pos].strip()
                if 0==0:
                     returnstring=returnlist=returnlist+[returnstring]
                     
                cursors=pos+1
                    
                ons=cursors
                
        else:
            returnstring=content[cursors:].strip()
            
            if 0==0:
                returnlist=returnlist+[returnstring]
            ttrue=False
    
    return returnlist
def adds(tree,n,counts,tabs,stack):
    if counts==1:
        if n.find("</")>-1:
            tabs-=1
            if tabs<0:
                tabs=0
            return tree,tabs,stack
        else:
            tabs=tabs+1  
    if tabs>len(stack):
        nodex=nodes(n.strip())
        stack[len(stack)-1].childs=nodex
        stack=stack+[nodex]
    elif tabs==len(stack):
        if tabs==len(stack):
            nodex=nodes(n.strip())
            stack[len(stack)-1].nexts=nodex
            stack[len(stack)-1]=nodex
    elif tabs<len(stack):
             ttrue=True
             nodex=None
             while ttrue:
                 if tabs<len(stack):
                     nodex=stack.pop()  
                 else:
                     ttrue=False
                 
             nodex=nodes(n.strip())
             stack[len(stack)-1].nexts=nodex
             stack[len(stack)-1]=nodex
    return tree,tabs,stack
def getScript(content, simbols1,simbols2):
    returnscript=[]
    ttrue=True
    pos=0
    pos2=0
    cursorStart=-1
    cursorEnd=-1
    while ttrue:
        cursorStart=-1
        cursorEnd=-1

        for n in simbols1:
            pos=content.find(n)
            if pos>-1:
                if cursorStart==-1:
                    cursorStart=pos
                elif pos<cursorStart:
                    cursorStart=pos
        for n in simbols2:
            pos2=content.find(n)
            if pos2>-1:
                if cursorEnd==-1:
                    cursorEnd=pos2
                elif pos2<cursorEnd:
                    cursorEnd=pos2
        if cursorStart>-1 and cursorEnd>-1:
            cursorEnd=cursorEnd+len(simbols2[0])
            returnscript=returnscript+[content[cursorStart:cursorEnd]]
            
            cont1=content[cursorEnd:]
            content=content[:cursorStart]+cont1
        else:
            ttrue=False 

            
    return returnscript,content
def processs(content):
    trees=nodes("html")
    stack=[trees]
    #get body only
    contentpos=content.find("<body")
    if contentpos<0:
        contentpos=content.find("<BODY")
    if contentpos>-1:
        content=content[contentpos:]
    contentpos=content.find("</body")
    
    if contentpos<0:
        contentpos=content.find("</BODY")
    if contentpos>-1:
        content=content[:contentpos]
    l1=["<script","<SCRIPT"]
    l2=["</script>","</SCRIPT>"]
    _,content=getScript(content, l1,l2)
    tabs=1
    l1=[">","'",'"']
    tags=attributs(content,l1)
    
    
    for tag in tags:
        l1=["<","'",'"']
        listtags=attributs(tag,l1)
        
        count=0
        for ttag in listtags:
            ttag=ttag.strip()
            if count==1:
                trees,tabs,stack=adds(trees,"<" + ttag + ">",count,tabs,stack)
            else:
                if ttag!="":
                    trees,tabs,stack=adds(trees,ttag,count,tabs,stack)
            count+=1
    return trees
files=input("give me a .html file? ")
f1=open(files,"r")
contents=f1.read()
f1.close()
contents=contents.replace("\n","\\n")
contents=contents.replace("\r","\\r")
contentss=processs(contents)
contentss.report()


