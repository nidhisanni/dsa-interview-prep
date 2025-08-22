arr=[1,2,3,4,5,8,6,0]
first= second= float('-inf')
for i in arr:
    if i > first:
        second= first
        first=i
    elif i > second and i !=first:
        second=i
print('SECOND LARGEST ELEMENT:', second)
        


arr=[1,2,3,4,5,8,6,0]
first= max(arr)
second= float('-inf')
for i in arr:
    if i !=first and i>second:
        second= i
print('SECOND LARGEST ELEMENT:', second)