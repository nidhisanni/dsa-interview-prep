arr=[1,2,3,4,5]
is_sorted= True    #Because we start by assuming that the array is sorted.
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted= False
        break;
if is_sorted == True:
    print('array is sorted!!')
else:
    print('array is not sorted')
