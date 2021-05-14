start = 99

for i in range(start+1):
    x = start - i
    if x == start:
        print(f"{x} bottles of beer on the wall, {x} bottles of beer.")
    elif x < start and x != 0:
        print(f"Take one down, pass it around, {x} bottles of beer on the wall...")
    elif x == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {start} bottles of beer on the wall...")


    
