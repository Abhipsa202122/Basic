a={"d":15,"m":4,"y":2022}
for i in a:
    b=a.get("y")
print(b)
#copy
a={"d":15,"m":4,"y":2022}
for i in a:
    b=a.copy()
print(b) 
#clear
a={"d":15,"m":4,"y":2022}
print(a.clear()) 

#pop
a={"d":15,"m":4,"y":2022}
b=a.pop("y") 
print(b)
#popitem
a={"d":15,"m":4,"y":2022}
b=a.popitem() 
print(b)
#del
a={"d":15,"m":4,"y":2022}

