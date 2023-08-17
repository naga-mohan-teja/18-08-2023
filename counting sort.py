arr=[8,1,2,2,3]
print(arr)
n=max(arr)
fre=[0]*(n+1)
print(fre)
for i in range(len(arr)):
    fre[arr[i]]+=1
print(fre)
#presum
ps=fre[::]
m=len(ps)
for j in range(1,m):
    ps[j]=ps[j]+ps[j-1]
print(ps)
ans=[0]*len(arr)
for i in range(len(arr)):
#     ans.append(ps[arr[i]]-fre[arr[i]])
# print(ans)
    ans[ps[arr[i]]-1]=arr[i]
    ps[arr[i]]-=1
print(ans)
