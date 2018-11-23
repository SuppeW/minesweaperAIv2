#Open neighbor of neighbor if neighor is 0.

import random, pygame

grid = []
bombs = 200


for i in range(0,20):
    grid.append([])
    for j in range(0,20):
        grid[i].append(0)

for i in range(0,bombs):
    grid[random.randint(0,19)][random.randint(0,19)] = 1




print(grid)


x = int(input("Velg celle fra 0 til 20, X = "))
y = int(input("Velg celle fra 0 til 20, Y = "))
teller = 0


if grid[y][x] == 0:
    for i in range(-1,2):
        for j in range(-1,2):
            if grid[y+i][x+j] == 0:
                for n in range(-1,2):
                    for p in range(-1,2):
                        if grid[y+i+n][x+j+p] == 0:
                            print(grid[y+i+n][x+j+p])
                            teller += 1

print(teller)
