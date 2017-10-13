neighbours = {}
cell_state = {}


def game():

    # 1 alive 0 dead
    # start when all cells are alive

    for i in range(1, 101):
        cell_state[i] = 1
        neighbours[i] = []

    # Add neigbours to every number

    for i in range(1, 101):
        # Handle the corners
        if i == 1:
            neighbours[i].append(i + 1)
            neighbours[i].append(i + 10)
            neighbours[i].append(i + 11)

        elif i == 10:
            neighbours[i].append(i - 1)
            neighbours[i].append(i + 9)
            neighbours[i].append(i + 10)

        elif i == 91:
            neighbours[i].append(i - 9)
            neighbours[i].append(i - 10)
            neighbours[i].append(i + 1)

        elif i == 100:
            neighbours[i].append(i - 11)
            neighbours[i].append(i - 1)
            neighbours[i].append(i - 10)

            # Cover 2-9
        elif i in range(2, 10, 1):
            neighbours[i].append(i - 1)
            neighbours[i].append(i + 1)
            neighbours[i].append(i + 9)
            neighbours[i].append(i + 10)
            neighbours[i].append(i + 11)

        # Handle the other regions on the outer part 11 - 81 step 10
        elif i in range(11, 82, 10):
            neighbours[i].append(i - 9)
            neighbours[i].append(i - 10)
            neighbours[i].append(i + 1)
            neighbours[i].append(i + 10)
            neighbours[i].append(i + 11)

        # Handle right end 20 to 90 step 10

        elif i in range(20, 91, 10):
            neighbours[i].append(i - 11)
            neighbours[i].append(i - 10)
            neighbours[i].append(i - 1)
            neighbours[i].append(i - 9)
            neighbours[i].append(i + 10)

        elif i in range(92, 100, 1):
            neighbours[i].append(i - 11)
            neighbours[i].append(i - 10)
            neighbours[i].append(i - 9)
            neighbours[i].append(i - 1)
            neighbours[i].append(i + 1)

        else:
            neighbours[i].append(i - 11)
            neighbours[i].append(i - 10)
            neighbours[i].append(i - 9)
            neighbours[i].append(i - 1)
            neighbours[i].append(i + 1)
            neighbours[i].append(i + 9)
            neighbours[i].append(i + 10)
            neighbours[i].append(i + 11)

    # sort table are you Dead or Alive
    for i in range(1, 101):
        list_neighbours = neighbours[i]
        count_live = 0
        # separate the live from the dead
        if cell_state[i] == 1:
            # check how many are alive and how many dead
            for my_neigbour in range(len(list_neighbours)):
                if cell_state[list_neighbours[my_neigbour]] == 1:
                    count_live += 1

            if count_live < 2:
                # less that 2 live neigb dies
                cell_state[i] = 0

            elif count_live > 3:
                cell_state[i] = 0

        else:
            for my_neigbour in range(len(list_neighbours)):
                if cell_state[list_neighbours[my_neigbour]] == 1:
                    count_live += 1

            if count_live == 3:
                cell_state[i] = 1

    # Now print the damn table
    for x in range(1, 11):
        for y in range(1, 11):
            print('|{:1}'.format(cell_state[x * y]), end=' ')
        print()


game()
