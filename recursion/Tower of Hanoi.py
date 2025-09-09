def tower_of_hanoi(n, source, helper, destination):
    #base case
    if n==1:
        print(f'move disk 1 from {source} -> {destination}')
        return
    
    else:
        tower_of_hanoi(n-1, source, destination, helper)
        
        print(f'move disk {n} from {source} -> {destination}')
        
        tower_of_hanoi(n-1, helper, source, destination)
        
tower_of_hanoi(3, 'A', 'B', 'C')