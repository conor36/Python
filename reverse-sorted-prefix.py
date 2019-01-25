a=[]
line=raw_input()

while line!= "end":
     a.append(int(line))
     line=raw_input()
i=0
while a[i]==a[i]+1:
     print a[(len(a)-1-i)]
     i+=1
     
