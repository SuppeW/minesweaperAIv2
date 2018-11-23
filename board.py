import random, pygame, time

rows = 18 + 2
cols = 18 + 2
bombs = 30



board=[]

for i in range(0,rows):
    board.append([])
    for j in range(0,cols):
        board[i].append(0)

for i in range(bombs):
    randx = int(random.randint(1,rows-2))
    randy = int(random.randint(1,cols-2))
    run = True
    while run:
        if board[randx][randy] == 9:
            randx,randy = random.randint(1,rows-2), random.randint(1,cols-2)
        else:
            board[randx][randy] = 9
            run = False

for r in range(0,rows-1):
    for c in range(0,cols-1):
        if board[r][c] == 9:
            continue
        else:
            for i in range(-1,2):
                for j in range(-1,2):
                    if board[r+i][c+j] == 9:
                        board[r][c] += 1

print(board)

pygame.init()

celldim = 20
boardsize = rows*celldim, cols*celldim
win = pygame.display.set_mode(boardsize)
pygame.display.set_caption("Mine Sweaper AI")
win.fill((255,255,255))
pygame.display.update()

liveCellColor = (200,200,200)
deadCellColor = (100,100,100)
bombSelectColor = (255,0,0)

font = pygame.font.SysFont(None, 30)


for i in range(0, rows):
    for j in range(0, cols):
        pygame.draw.rect(win, liveCellColor,(i*celldim, j*celldim, celldim-1, celldim-1))

pygame.display.update()

run = True
while run:
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x,y= pygame.mouse.get_pos()
            x,y = int(x/celldim), int(y/celldim)
            board[y][x] = 10
            pygame.draw.rect(win, bombSelectColor,(x*celldim, y*celldim, celldim-1, celldim-1))
            pygame.display.update()

            print(board[y][x])

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #
            # FINNE DOKUMENTASJON PÅ HVORDAN MAN FIKSER LEFTMOUSEBUTTON LISTENER.
            # FIKSE, AT NABO NULL ÅPNER NY NABO NULL, ON AND ON.
            # FIKSE START OG SLUTT SKJERM.
            # KOBLE OPP MOT AI
            # KJØRE BOARD.PY FRA EN ANNEN PYTHON FIL.
            #

            x,y= pygame.mouse.get_pos()
            x,y = int(x/celldim), int(y/celldim)
            print("*****")
            print(x,y)
            print("*****")

            if board[y][x] == 9:
                pygame.draw.rect(win, deadCellColor,(x*celldim, y*celldim, celldim-1, celldim-1))
                text = font.render(str(board[y][x]), True, (255,255,255))
                win.blit(text,((x*celldim)+4, y*celldim))
                pygame.display.update()
                print("You lost the game!")
                time.sleep(1)
                pygame.quit()
            elif board[y][x] == 0:
                for i in range(-1,2):
                    for j in range(-1,2):
                        r, c = x+i, y+j
                        if board[c][r] == 0:
                            pygame.draw.rect(win, deadCellColor,(r*celldim, c*celldim, celldim-1, celldim-1))
                            pygame.display.update()
                        elif board[c][r] == 10:
                            pygame.draw.rect(win, bombSelectColor,(r*celldim, c*celldim, celldim-1, celldim-1))
                            pygame.display.update()

                        else:
                            pygame.draw.rect(win, deadCellColor,(r*celldim, c*celldim, celldim-1, celldim-1))
                            text = font.render(str(board[c][r]), True, (255,255,255))
                            win.blit(text,((r*celldim)+4, c*celldim))
                            pygame.display.update()



            else:
                pygame.draw.rect(win, deadCellColor,(x*celldim, y*celldim, celldim-1, celldim-1))
                text = font.render(str(board[y][x]), True, (255,255,255))
                win.blit(text,((x*celldim)+4, y*celldim))
                pygame.display.update()
                print(x,y)

pygame.quit()
