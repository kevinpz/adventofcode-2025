def main():
    batteries = []
    max_power = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f:
            batteries.append(line.replace("\n", ""))

    # For each battery line
    for battery in batteries:
        max_b = []
        idx = 0
        # For the first 11 cells
        for nb in range(11):
            # Find the max cell allowing nb more cells
            cur_b = max(list(battery[:-11+nb]))
            max_b.append(cur_b)
            # Continue with the remaining cells
            battery = battery[battery.index(cur_b)+1:]
        
        # For the last one just find the max in the remaining cells
        max_b.append(max(list(battery)))
        # Add the max power of the battery
        max_power += int(''.join(max_b))

    print(max_power)

if __name__ == "__main__":  
    main()
