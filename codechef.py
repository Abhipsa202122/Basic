# a=int(input("enter"))
# for i in range(a):
#     n=int(input())
#     l=list(map(int,input().split()))
#     # s=sum(l) 

b=[1,2,3,4,5]
def fun(n):
    return n+2
result=list(map(fun,b))
#s=sum(result)
b=result.count(2)
#result=list(map(lambda n: n+2 a))
#result=list(map(lambda n,m: n+m,a,b))
print(result)
print(type(result))
for i in result:
    print(i)
#1.make the sum of even
a=int(input())
for i in range(a):
    n=int(input())
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
t = int(input("how much time code will run :"))
while(t>0):
    cats, dogs, legs = map(int, input(" :-").split())
    max_legs = (dogs + cats) * 4
 
    if((2 * dogs) >= cats):
        min_legs = 4 * dogs

    else:
        min_legs = (cats - (2*dogs)) * 4 + dogs * 4

    if(legs < min_legs or legs > max_legs):
        print("no")

    else:
        if(legs % 4 == 0):
            print("yes")
        else:
            print("no")
    t -= 1            
a=int(input())
b=int(input()) 
a,b=map(int,input().split())           

        
