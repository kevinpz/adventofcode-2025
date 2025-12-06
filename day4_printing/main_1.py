def main():
    paper_list = []
    paper_nb = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f:
            # Convert the data to 0 and 1
            data = line.replace("\n", "")
            data = data.replace(".", "0")
            data = data.replace("@", "1")
            # Add a dummy border
            paper_list.append(f'0{data}0')


    paper_x = len(paper_list[0]) - 2
    paper_y = len(paper_list)
    line_to_add = '0' * (paper_x + 2)
    # Add a dummy border
    paper_list = [line_to_add] + paper_list + [line_to_add]

    for i in range(1, paper_y + 1):
        for j in range(1, paper_x + 1):
            # Check if the cell is a @
            if paper_list[i][j] == '1':
                # Count the number of @ around the cell
                total_around = int(paper_list[i-1][j-1]) + int(paper_list[i-1][j]) + int(paper_list[i-1][j+1]) + int(paper_list[i][j-1]) + int(paper_list[i][j+1]) + int(paper_list[i+1][j-1]) + int(paper_list[i+1][j]) + int(paper_list[i+1][j+1])
                if total_around < 4:
                    paper_nb += 1

    print(paper_nb)

if __name__ == "__main__":  
    main()
