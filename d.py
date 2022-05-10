a={"a":8,"b":9,"c":10,"d":6}
d={"e":11}
for i in (a,d):
    a.update(d)
print(a)
#without update:
a={"a":8,"b":9,"c":10,"d":6}
b={"e":11}
d={}
for i in a:
    d[i]=a[i]
    for j in b:
        d[j]=b[j]
print(d)        
