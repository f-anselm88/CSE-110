points_scored = [10, 20, 15, 30, 25]

running_total = 0
for points in points_scored:
    running_total += points #This is the same as running_total = running_total + points
    
print(f"The player has scored: {running_total}")