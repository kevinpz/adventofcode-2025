def main():
    pos = 50
    code = 0
    with open("input.txt", "r") as f:
        for line in f:
            direction = line[0]
            steps = int(line[1:])

            if direction == "L":
                steps *= -1

            tmp_pos = pos + steps
            
            # count if we pass 0 from going between positive and negative
            if 0 in range(min(pos, tmp_pos)+1, max(pos, tmp_pos)): 
                code += 1

            pos = tmp_pos % 100
            # if we have a big rotation count how many times we pass 0
            if abs(tmp_pos) >= 100:
                code += abs(tmp_pos) // 100
            # if it's a small rotation and we end up at 0 count it
            elif pos == 0:
                code += 1

    print(code)


if __name__ == "__main__":  
    main()
