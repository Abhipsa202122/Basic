# a=input("enter name")
# #x=["abhi"]
# l=[]
# for i in a:
#     b=ord(i)
#     if (i>="A" and i<="Z"):
#         l.append(b-64)
#     else:
#         l.append(b-96)
# print(l)
a=int(input("enter no"))
# s=0
# while i <= i:
#     if i%2==0:
#         s=s+i
#     i+=1    
# print("even",s)
for _ in range(a):
    n=int(input("enter no"))
    l=list(map(int,input().split()))
    
    s=sum(l) 
    b=l.count(2)
    if s%2==0:
        print(0)
    else:
        if s%2==1 and b!=0:
            print(1)
        else:
            print(-1)
