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

            # Iterate over all length for current number
            for j in range(1,len(nb)):
                nb_split = [nb[k:k+j] for k in range(0, len(nb), j)]
                nb_unique = set(nb_split)
                if len(nb_unique) == 1:
                    invalid_ids += i
                    break

    
    print(invalid_ids)


if __name__ == "__main__":  
    main()