arr=[7,4,5,1,3]
for i in range(len(arr)):
  for j in range(i):
    if arr[j]>arr[i]:
       arr[j],arr[i]=arr[i],arr[j]
print(arr)
