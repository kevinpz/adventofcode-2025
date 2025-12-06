def main():
    fresh_foods = []
    range_done = []
    result = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f:
            if "-" in line:
                start, end = line.split("-")
                fresh_foods.append([int(start), int(end)])


    for start, end in fresh_foods:

        # If we already have done a part of the start of the range, we skip it
        for start_done, end_done in range_done:
            if start >= start_done and start <= end_done:
                start = end_done + 1

            # If we already have done a part of the end of the range, we skip it
            if end >= start_done and end <= end_done:
                end = start_done - 1

            # If we already have a subrange included in the current range, we remove it from the total
            if start < start_done and end > end_done:
                result -= end_done - start_done + 1
                

        # If the range is valid, we add it to the total
        if start <= end:
            result += end - start + 1
            range_done.append([start, end])
        
    print(result)

if __name__ == "__main__":  
    main()
