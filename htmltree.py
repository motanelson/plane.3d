
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
    tabs=1
    tags=content.split(">")
    for tag in tags:
        listtags=tag.split("<")
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
content=processs(contents)
content.report()


