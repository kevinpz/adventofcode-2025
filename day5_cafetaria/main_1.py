def main():
    fresh_foods = []
    available_foods = []
    result = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f:
            if "-" in line:
                start, end = line.split("-")
                fresh_foods.append([int(start), int(end)])
            elif line[0] != "\n":
                available_foods.append(int(line))

    for food in available_foods:
        for fresh in fresh_foods:
            if food >= fresh[0] and food <= fresh[1]:
                result += 1
                break

    print(result)

if __name__ == "__main__":  
    main()
