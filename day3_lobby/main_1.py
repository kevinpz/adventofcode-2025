def main():
    batteries = []
    max_power = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f:
            batteries.append(line.replace("\n", ""))

    for battery in batteries:
        b_list = list(battery)
        # Find the first battery with max power
        max_b1 = max(b_list[0:-1])
        pos = b_list.index(max_b1)
        max_b2 = max(b_list[pos+1:])

        max_power += (int(max_b1) * 10 + int(max_b2))
    print(max_power)

if __name__ == "__main__":  
    main()
