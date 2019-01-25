a=[]
line=raw_input()

if len(a)!=0:
   while line!="end":
      a.append(int(line))
      line=raw_input()

i=0
while i<len(a):
    p=i
    j=i+1
    while j<len(a):
        if a[j] <a[p]:
            p=j
        j=j+1
    

        tmp=a[p]
        a[p]=a[i]
        a[i]=tmp
      
        i+=1

print a[m]
