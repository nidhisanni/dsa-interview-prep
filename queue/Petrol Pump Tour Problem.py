def petrol_pump_tour(petrol, distance):
    n = len(petrol)
    start = 0
    balance = 0
    deficit = 0

    for i in range(n):
        balance += petrol[i] - distance[i]
        
        # if balance goes negative, reset start
        if balance < 0:
            start = i + 1
            deficit += balance
            balance = 0
    
    # If total fuel >= total distance → possible
    if balance + deficit >= 0:
        return start
    else:
        return -1  # not possible

# Example
petrol = [4, 6, 7, 4]
distance = [6, 5, 3, 5]
print(petrol_pump_tour(petrol, distance))
