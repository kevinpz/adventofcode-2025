def main():
    invalid_ids = 0

    # Read input
    with open("input.txt", "r") as f:
        input=f.read()

    # Split input
    ranges = input.split(",")
    for r in ranges:
        start, end = map(int, r.split("-")) # Get start and end in int

        # Iterate over range
        for i in range(start, end + 1):
            nb = str(i)
            # Check if half of the number is equal to the other half
            if nb[0:len(nb)//2] == nb[len(nb)//2:]:
                invalid_ids += int(nb)

    
    print(invalid_ids)


if __name__ == "__main__":  
    main()
