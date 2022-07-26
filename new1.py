##missing no


n=[3,7,1,2,8,4,5]
n.sort()
print(n)  #[1,2,3,4,5,7,8]

n1=n[-1]
#print(n1)
#sum=n(n+1)


sum=n1*(n1+1)//2
Total=0
for x in n:
    Total=Total+x

miss=sum-Total
print(miss) 



