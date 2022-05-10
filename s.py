a={"a":10,"b":{"c":30,"d":50}}
#a=[10,20,[30,40,50]]
s=0
for i in a:
    if type(a[i])==type({}):
       for j in a[i]:
           s=s+a[i][j]
    #else:
        #s+=a[i]
print(s) 

# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(end=" ")
# 		b=b+1
# 	j=1
# 	while j<=i:
# 		print('*',end=" ")
# 		j=j+1
# 	i=i+1
# 	print()
# c=4
# while c>=1:
# 	d=1
# 	while d<=4:
# 		print(end=" ")
# 		d=d+1
# 	f=1
# 	while d<=c:
# 		print('*',end=" ")
# 		f=f+1
# 	d=d+1
# 	print()



