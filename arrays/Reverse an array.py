arr=[1,2,3,4,5]
start=0
end=len(arr)-1
while start < end:    #A while loop keeps running as long as the condition is True.
    arr[start], arr[end]= arr[end], arr[start]
    start= start+1
    end= end-1
print('reversed array: ', arr)