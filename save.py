
class nodes:
    def __init__(self,value):
        self.value=value
        self.nexts=None
        self.childs=None
    def __repr__ (self,values):
        values=""
        if self.nexts!=None:
            values=values+self.value+"\n"
            self.nexts.__repr__(values)
            
        return values

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

    def save(self,name):
        stack=[]
        ttrue=True
        back=self
        contents=""
        while ttrue:
            
            if back!=None:
                if back.value!="tree":
                    contents=contents+" "*len(stack)+back.value+"\n"
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
        f1=open(name,"w")
        f1.write(contents)
        f1.close()   
           
           
tree=nodes("tree")
arm=nodes("ARM")
X86=nodes("x86")
tree.childs=arm
arm.nexts=X86
arm7=nodes("arm 7")
arm8=nodes("arm 8")
arm.childs=arm7
arm7.nexts=arm8
x8086=nodes("8086")
X86.childs=x8086
x80186=nodes("80186")
x8086.nexts=x80186
x80286=nodes("80286")
x80186.nexts=x80286
x80386=nodes("80386")
x80286.nexts=x80386
x80486=nodes("80486")
x80386.nexts=x80486


back=tree

tree.save("saves.txt")
