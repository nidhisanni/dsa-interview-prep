def print_list(list, idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)
    
nos= [1,2,3,4,5,6,77]
print(print_list(nos, 0))