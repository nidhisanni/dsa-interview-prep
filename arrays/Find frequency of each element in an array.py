arr = [1, 2, 2, 3, 1, 4, 2]
freq= {}
for i in arr:
    if i in freq:
        freq[i] = freq[i] + 1        #for dictionaries, [] means "key"
    else:
        freq[i] = 1
for key in freq:
    print(f'{key}:{freq[key]} times')
