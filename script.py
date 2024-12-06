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
    scripts,content=getScript(content, l1,l2)
    
    
    return scripts
files=input("give me a .html file? ")
f1=open(files,"r")
contents=f1.read()
f1.close()
contents=contents.replace("\n","\\n")
contents=contents.replace("\r","\\r")
contentss=processs(contents)
print("-----------------------------------------------------------------")

for content in contentss:
    print(content)
    print("-----------------------------------------------------------------")

