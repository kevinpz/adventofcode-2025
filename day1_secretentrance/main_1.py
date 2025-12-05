def main():
    pos = 50
    code = 0
    with open("input.txt", "r") as f:
        for line in f:
            direction = line[0]
            steps = int(line[1:])

            if direction == "L":
                steps *= -1

            pos = (pos + steps) % 100
            # count how many time we end up at 0
            if pos == 0:
                code +=1

    print(code)


if __name__ == "__main__":  
    main()
