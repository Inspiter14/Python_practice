class StringOper:
    def inputstr(self):
        str=input("Enter a String: ")
        return str

    def split(self,str,delimeter=' \t\n'):
        split_val=[]
        word=''
        for c in str:
            if c==' ':
                split_val.append(word)
                word=''
            else:
                word+=c
        if word:
            split_val.append(word)
        return split_val

    def findlen(self,str):
        cnt=0
        for i in str:
            cnt=cnt+1
        return cnt

    def longword(self,str):
        length=0
        split_vals=[]
        split_vals=self.split(str)
        for i in split_vals:
            n=self.findlen(i)
            if n>length:
                length=n
                word=i
        print(word)

    def findfreq(self,str):
        b=input("Enter character to find frequency: ")
        c=0
        for i in str:
            if i==b:
                c+=1
        print(c)

    def palindrom(self):
        chr=input("Enter a Word:")
        if chr==chr[::-1]:
            print("Strinf is Palindrom")
        else:
            print("Not Palindrom")


s=StringOper()
st=s.inputstr()
#s.split(st)
s.longword(st)
s.findfreq(st)
s.palindrom()