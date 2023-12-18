import random, time, pygame, sys, copy
from pygame.locals import *

FPS = 30 # frames per second to update the screen
WINDOWWIDTH = 1000  # width of the program's window, in pixels
WINDOWHEIGHT = 1000 # height in pixels

BOARDWIDTH = 6 # how many columns in the board
BOARDHEIGHT = 6 # how many rows in the board
IMAGESIZE = 128 # width & height of each space in pixels

# NUMTEACHERIMAGES is the number of TEACHER types. You will need .png image
# files named TEACHER0.png, TEACHER1.png, etc. up to TEACHER(N-1).png.
NUMIMAGES = 7
assert NUMIMAGES >= 5 # game needs at least 5 types of TEACHERs to work

# NUMMATCHSOUNDS is the number of different sounds to choose from when
# a match is made. The .wav files are named match0.wav, match1.wav, etc.
NUMMATCHSOUNDS = 6

MOVERATE = 25 # 1 to 100, larger num means faster animations
DEDUCTSPEED = 0.8 # reduces score by 1 point every DEDUCTSPEED seconds.

#             R    G    B
PURPLE    = (255,   0, 255)
LIGHTBLUE = (170, 190, 255)
BLUE      = (  0,   0, 255)
RED       = (255, 100, 100)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)
HIGHLIGHTCOLOR = PURPLE # color of the selected TEACHER's border
BGCOLOR = LIGHTBLUE # background color on the screen
GRIDCOLOR = BLUE # color of the game board
GAMEOVERCOLOR = RED # color of the "Game over" text.
GAMEOVERBGCOLOR = BLACK # background color of the "Game over" text.
SCORECOLOR = BROWN # color of the text for the player's score

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
XMARGIN = int((WINDOWWIDTH - IMAGESIZE * BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - IMAGESIZE * BOARDHEIGHT) / 2)

# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

EMPTY_SPACE = -1 # an arbitrary, nonpositive value
ROWABOVEBOARD = 'row above board' # an arbitrary, noninteger value

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGES, GAMESOUNDS, BASICFONT, BOARDRECTS

    # Initial set up.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Match Masters')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)

    # Load the images
    # Učitaj slike i obradi njihovu veličinu
    IMAGES = []
    for i in range(1, NUMIMAGES + 1):
        Image = pygame.image.load('teniser%s.png' % i)
        if Image.get_size() != (IMAGESIZE, IMAGESIZE):
            width, height = Image.get_size()
            if width < IMAGESIZE or height < IMAGESIZE:
                Image = pygame.transform.scale(Image, (IMAGESIZE, IMAGESIZE))
            else:
                Image = Image.subsurface((0, 0, IMAGESIZE, IMAGESIZE))
        IMAGES.append(Image)


    # Load the sounds.
    GAMESOUNDS = {}
    GAMESOUNDS['bad swap'] = pygame.mixer.Sound('badswap.wav')
    GAMESOUNDS['match'] = []
    for i in range(NUMMATCHSOUNDS):
        GAMESOUNDS['match'].append(pygame.mixer.Sound('match%s.wav' % i))

    # Create pygame.Rect objects for each board space to
    # do board-coordinate-to-pixel-coordinate conversions.
    BOARDRECTS = []
    for x in range(BOARDWIDTH):
        BOARDRECTS.append([])
        for y in range(BOARDHEIGHT):
            r = pygame.Rect((XMARGIN + (x * IMAGESIZE),
                             YMARGIN + (y * IMAGESIZE),
                             IMAGESIZE,
                             IMAGESIZE))
            BOARDRECTS[x].append(r)

    while True:
        runGame()


def runGame():
    # Plays through a single game. When the game is over, this function returns.

    # initalize the board
    gameBoard = getBlankBoard()
    score = 0
    fillBoardAndAnimate(gameBoard, [], score) # Drop the initial TEACHERs.

    # initialize variables for the start of a new game
    firstSelected = None
    lastMouseDownX = None
    lastMouseDownY = None
    gameIsOver = False
    lastScoreDeduction = time.time()
    clickContinueTextSurf = None

    while True: # main game loop
        clickedSpace = None
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_BACKSPACE:
                return # start a new game

            elif event.type == MOUSEBUTTONUP:
                if gameIsOver:
                    return # after games ends, click to start a new game

                if event.pos == (lastMouseDownX, lastMouseDownY):
                    # This event is a mouse click, not the end of a mouse drag.
                    clickedSpace = checkForClick(event.pos)
                else:
                    # this is the end of a mouse drag
                    firstSelected = checkForClick((lastMouseDownX, lastMouseDownY))
                    clickedSpace = checkForClick(event.pos)
                    if not firstSelected or not clickedSpace:
                        # if not part of a valid drag, deselect both
                        firstSelected = None
                        clickedSpace = None
            elif event.type == MOUSEBUTTONDOWN:
                # this is the start of a mouse click or mouse drag
                lastMouseDownX, lastMouseDownY = event.pos

        if clickedSpace and not firstSelected:
            # This was the first TEACHER clicked on.
            firstSelected = clickedSpace
        elif clickedSpace and firstSelected:
            # Two TEACHERs have been clicked on and selected. Swap the TEACHERs.
            firstSwapping, secondSwapping = getSwapping(gameBoard, firstSelected, clickedSpace)
            if firstSwapping == None and secondSwapping == None:
                # If both are None, then the TEACHERs were not adjacent
                firstSelected = None # deselect the first TEACHER
                continue

            # Show the swap animation on the screen.
            boardCopy = getBoardCopyMinusTEACHERs(gameBoard, (firstSwapping, secondSwapping))
            animateMoving(boardCopy, [firstSwapping, secondSwapping], [], score)

            # Swap the TEACHERs in the board data structure.
            gameBoard[firstSwapping['x']][firstSwapping['y']] = secondSwapping['imageNum']
            gameBoard[secondSwapping['x']][secondSwapping['y']] = firstSwapping['imageNum']

            # See if this is a matching move.
            matched = findMatching(gameBoard)
            if matched == []:
                # Was not a matching move; swap the TEACHERs back
                GAMESOUNDS['bad swap'].play()
                animateMoving(boardCopy, [firstSwapping, secondSwapping], [], score)
                gameBoard[firstSwapping['x']][firstSwapping['y']] = firstSwapping['imageNum']
                gameBoard[secondSwapping['x']][secondSwapping['y']] = secondSwapping['imageNum']
            else:
                # This was a matching move.
                scoreAdd = 0
                while matched != []:
                    # Remove matched TEACHERs, then pull down the board.

                    # points is a list of dicts that tells fillBoardAndAnimate()
                    # where on the screen to display text to show how many
                    # points the player got. points is a list because if
                    # the playergets multiple matches, then multiple points text should appear.
                    points = []
                    for image_set in matched:
                        scoreAdd += (10 + (len(image_set) - 3) * 10)
                        for tennis_player in image_set:
                            gameBoard[tennis_player[0]][tennis_player[1]] = EMPTY_SPACE
                        points.append({'points': scoreAdd,
                                       'x': tennis_player[0] * IMAGESIZE + XMARGIN,
                                       'y': tennis_player[1] * IMAGESIZE + YMARGIN})
                    random.choice(GAMESOUNDS['match']).play()
                    score += scoreAdd

                    # Drop the new TEACHERs.
                    fillBoardAndAnimate(gameBoard, points, score)

                    # Check if there are any new matches.
                    matched = findMatching(gameBoard)
            firstSelected = None

            if not canMakeMove(gameBoard):
                gameIsOver = True

        # Draw the board.
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(gameBoard)
        if firstSelected != None:
            highlightSpace(firstSelected['x'], firstSelected['y'])
        if gameIsOver:
            if clickContinueTextSurf == None:
                # Only render the text once. In future iterations, just
                # use the Surface object already in clickContinueTextSurf
                clickContinueTextSurf = BASICFONT.render('Final Score: %s (Click to continue)' % (score), 1, GAMEOVERCOLOR, GAMEOVERBGCOLOR)
                clickContinueTextRect = clickContinueTextSurf.get_rect()
                clickContinueTextRect.center = int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2)
            DISPLAYSURF.blit(clickContinueTextSurf, clickContinueTextRect)
        elif score > 0 and time.time() - lastScoreDeduction > DEDUCTSPEED:
            # score drops over time
            score -= 1
            lastScoreDeduction = time.time()
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def getSwapping(board, firstXY, secondXY):
    # If the TEACHERs at the (X, Y) coordinates of the two TEACHERs are adjacent,
    # then their 'direction' keys are set to the appropriate direction
    # value to be swapped with each other.
    # Otherwise, (None, None) is returned.
    first = {'imageNum': board[firstXY['x']][firstXY['y']],
                    'x': firstXY['x'],
                    'y': firstXY['y']}
    second = {'imageNum': board[secondXY['x']][secondXY['y']],
                     'x': secondXY['x'],
                     'y': secondXY['y']}

    if first['x'] == second['x'] + 1 and first['y'] == second['y']:
        first['direction'] = LEFT
        second['direction'] = RIGHT
    elif first['x'] == second['x'] - 1 and first['y'] == second['y']:
        first['direction'] = RIGHT
        second['direction'] = LEFT
    elif first['y'] == second['y'] + 1 and first['x'] == second['x']:
        first['direction'] = UP
        second['direction'] = DOWN
    elif first['y'] == second['y'] - 1 and first['x'] == second['x']:
        first['direction'] = DOWN
        second['direction'] = UP
    else:
        # These TEACHERs are not adjacent and can't be swapped.
        return None, None
    return first, second


def getBlankBoard():
    # Create and return a blank board data structure.
    board = []
    for x in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)
    return board


def canMakeMove(board):
    # Return True if the board is in a state where a matching
    # move can be made on it. Otherwise return False.

    # The patterns in oneOffPatterns represent TEACHERs that are configured
    # in a way where it only takes one move to make a triplet.
    oneOffPatterns = (((0,1), (1,0), (2,0)),
                      ((0,1), (1,1), (2,0)),
                      ((0,0), (1,1), (2,0)),
                      ((0,1), (1,0), (2,1)),
                      ((0,0), (1,0), (2,1)),
                      ((0,0), (1,1), (2,1)),
                      ((0,0), (0,2), (0,3)),
                      ((0,0), (0,1), (0,3)))

    # The x and y variables iterate over each space on the board.
    # If we use + to represent the currently iterated space on the
    # board, then this pattern: ((0,1), (1,0), (2,0))refers to identical
    # TEACHERs being set up like this:
    #
    #     +A
    #     B
    #     C
    #
    # That is, TEACHER A is offset from the + by (0,1), TEACHER B is offset
    # by (1,0), and TEACHER C is offset by (2,0). In this case, TEACHER A can
    # be swapped to the left to form a vertical three-in-a-row triplet.
    #
    # There are eight possible ways for the TEACHERs to be one move
    # away from forming a triple, hence oneOffPattern has 8 patterns.

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            for pat in oneOffPatterns:
                # check each possible pattern of "match in next move" to
                # see if a possible move can be made.
                if (get_tennis_player(board, x + pat[0][0], y + pat[0][1]) == \
                    get_tennis_player(board, x + pat[1][0], y + pat[1][1]) == \
                    get_tennis_player(board, x + pat[2][0], y + pat[2][1]) != None) or \
                        (get_tennis_player(board, x + pat[0][1], y + pat[0][0]) == \
                         get_tennis_player(board, x + pat[1][1], y + pat[1][0]) == \
                         get_tennis_player(board, x + pat[2][1], y + pat[2][0]) != None):
                    print(x,y,pat)
                    return True # return True the first time you find a pattern
    return False


def drawMovingPlayer(player, progress):
    # Draw a TEACHER sliding in the direction that its 'direction' key
    # indicates. The progress parameter is a number from 0 (just
    # starting) to 100 (slide complete).
    movex = 0
    movey = 0
    progress *= 0.01

    if player['direction'] == UP:
        movey = -int(progress * IMAGESIZE)
    elif player['direction'] == DOWN:
        movey = int(progress * IMAGESIZE)
    elif player['direction'] == RIGHT:
        movex = int(progress * IMAGESIZE)
    elif player['direction'] == LEFT:
        movex = -int(progress * IMAGESIZE)

    basex = player['x']
    basey = player['y']
    if basey == ROWABOVEBOARD:
        basey = -1

    pixelx = XMARGIN + (basex * IMAGESIZE)
    pixely = YMARGIN + (basey * IMAGESIZE)
    r = pygame.Rect((pixelx + movex, pixely + movey, IMAGESIZE, IMAGESIZE))
    DISPLAYSURF.blit(IMAGES[player['imageNum']], r)


def pullDownAllPlayers(board):
    # pulls down TEACHERs on the board to the bottom to fill in any gaps
    for x in range(BOARDWIDTH):
        PlayersInColumn = []
        for y in range(BOARDHEIGHT):
            if board[x][y] != EMPTY_SPACE:
                PlayersInColumn.append(board[x][y])
        board[x] = ([EMPTY_SPACE] * (BOARDHEIGHT - len(PlayersInColumn))) + PlayersInColumn


def get_tennis_player(board, x, y):
    if x < 0 or y < 0 or x >= BOARDWIDTH or y >= BOARDHEIGHT:
        return None
    else:
        return board[x][y]


def getDropSlots(board):
    # Creates a "drop slot" for each column and fills the slot with a
    # number of TEACHERs that that column is lacking. This function assumes
    # that the TEACHERs have been gravity dropped already.
    boardCopy = copy.deepcopy(board)
    pullDownAllPlayers(boardCopy)

    dropSlots = []
    for i in range(BOARDWIDTH):
        dropSlots.append([])

    # count the number of empty spaces in each column on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT-1, -1, -1): # start from bottom, going up
            if boardCopy[x][y] == EMPTY_SPACE:
                possible_player = list(range(len(IMAGES)))
                for offsetX, offsetY in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                    # Narrow down the possible TEACHERs we should put in the
                    # blank space so we don't end up putting an two of
                    # the same TEACHERs next to each other when they drop.
                    neighbor_player = get_tennis_player(boardCopy, x + offsetX, y + offsetY)
                    if neighbor_player != None and neighbor_player in possible_player:
                        possible_player.remove(neighbor_player)

                new_player = random.choice(possible_player)
                boardCopy[x][y] = new_player
                dropSlots[x].append(new_player)
    return dropSlots


def findMatching(board):
    playersToRemove = [] # a list of lists of TEACHERs in matching triplets that should be removed
    boardCopy = copy.deepcopy(board)

    # loop through each space, checking for 3 adjacent identical TEACHERs
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            # look for horizontal matches
            if get_tennis_player(boardCopy, x, y) == get_tennis_player(boardCopy, x + 1, y) == get_tennis_player(boardCopy, x + 2, y) and get_tennis_player(boardCopy, x, y) != EMPTY_SPACE:
                target_player = boardCopy[x][y]
                offset = 0
                removeSet = []
                while get_tennis_player(boardCopy, x + offset, y) == target_player:
                    # keep checking if there's more than 3 TEACHERs in a row
                    removeSet.append((x + offset, y))
                    boardCopy[x + offset][y] = EMPTY_SPACE
                    offset += 1
                playersToRemove.append(removeSet)

            # look for vertical matches
            if get_tennis_player(boardCopy, x, y) == get_tennis_player(boardCopy, x, y + 1) == get_tennis_player(boardCopy, x, y + 2) and get_tennis_player(boardCopy, x, y) != EMPTY_SPACE:
                target_player = boardCopy[x][y]
                offset = 0
                removeSet = []
                while get_tennis_player(boardCopy, x, y + offset) == target_player:
                    # keep checking, in case there's more than 3 TEACHERs in a row
                    removeSet.append((x, y + offset))
                    boardCopy[x][y + offset] = EMPTY_SPACE
                    offset += 1
                playersToRemove.append(removeSet)

    return playersToRemove


def highlightSpace(x, y):
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, BOARDRECTS[x][y], 4)


def getDroppingTEACHERs(board):
    # Find all the TEACHERs that have an empty space below them
    boardCopy = copy.deepcopy(board)
    dropping_players = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 2, -1, -1):
            if boardCopy[x][y + 1] == EMPTY_SPACE and boardCopy[x][y] != EMPTY_SPACE:
                # This space drops if not empty but the space below it is
                dropping_players.append({'imageNum': boardCopy[x][y], 'x': x, 'y': y, 'direction': DOWN})
                boardCopy[x][y] = EMPTY_SPACE
    return dropping_players


def animateMoving(board, players, pointsText, score):
    # pointsText is a dictionary with keys 'x', 'y', and 'points'
    progress = 0 # progress at 0 represents beginning, 100 means finished.
    while progress < 100: # animation loop
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        for TEACHER in players: # Draw each TEACHER.
            drawMovingPlayer(TEACHER, progress)
        drawScore(score)
        for pointText in pointsText:
            pointsSurf = BASICFONT.render(str(pointText['points']), 1, SCORECOLOR)
            pointsRect = pointsSurf.get_rect()
            pointsRect.center = (pointText['x'], pointText['y'])
            DISPLAYSURF.blit(pointsSurf, pointsRect)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        progress += MOVERATE # progress the animation a little bit more for the next frame


def moveTEACHERs(board, movingTEACHERs):
    # movingTEACHERs is a list of dicts with keys x, y, direction, imageNum
    for TEACHER in movingTEACHERs:
        if TEACHER['y'] != ROWABOVEBOARD:
            board[TEACHER['x']][TEACHER['y']] = EMPTY_SPACE
            movex = 0
            movey = 0
            if TEACHER['direction'] == LEFT:
                movex = -1
            elif TEACHER['direction'] == RIGHT:
                movex = 1
            elif TEACHER['direction'] == DOWN:
                movey = 1
            elif TEACHER['direction'] == UP:
                movey = -1
            board[TEACHER['x'] + movex][TEACHER['y'] + movey] = TEACHER['imageNum']
        else:
            # TEACHER is located above the board (where new TEACHERs come from)
            board[TEACHER['x']][0] = TEACHER['imageNum'] # move to top row


def fillBoardAndAnimate(board, points, score):
    dropSlots = getDropSlots(board)
    while dropSlots != [[]] * BOARDWIDTH:
        # do the dropping animation as long as there are more TEACHERs to drop
        movingTEACHERs = getDroppingTEACHERs(board)
        for x in range(len(dropSlots)):
            if len(dropSlots[x]) != 0:
                # cause the lowest TEACHER in each slot to begin moving in the DOWN direction
                movingTEACHERs.append({'imageNum': dropSlots[x][0], 'x': x, 'y': ROWABOVEBOARD, 'direction': DOWN})

        boardCopy = getBoardCopyMinusTEACHERs(board, movingTEACHERs)
        animateMoving(boardCopy, movingTEACHERs, points, score)
        moveTEACHERs(board, movingTEACHERs)

        # Make the next row of TEACHERs from the drop slots
        # the lowest by deleting the previous lowest TEACHERs.
        for x in range(len(dropSlots)):
            if len(dropSlots[x]) == 0:
                continue
            board[x][0] = dropSlots[x][0]
            del dropSlots[x][0]


def checkForClick(pos):
    # See if the mouse click was on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if BOARDRECTS[x][y].collidepoint(pos[0], pos[1]):
                return {'x': x, 'y': y}
    return None # Click was not on the board.


def drawBoard(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            pygame.draw.rect(DISPLAYSURF, GRIDCOLOR, BOARDRECTS[x][y], 1)
            TEACHERToDraw = board[x][y]
            if TEACHERToDraw != EMPTY_SPACE:
                DISPLAYSURF.blit(IMAGES[TEACHERToDraw], BOARDRECTS[x][y])


def getBoardCopyMinusTEACHERs(board, TEACHERs):
    # Creates and returns a copy of the passed board data structure,
    # with the TEACHERs in the "TEACHERs" list removed from it.
    #
    # TEACHERs is a list of dicts, with keys x, y, direction, imageNum

    boardCopy = copy.deepcopy(board)

    # Remove some of the TEACHERs from this board data structure copy.
    for TEACHER in TEACHERs:
        if TEACHER['y'] != ROWABOVEBOARD:
            boardCopy[TEACHER['x']][TEACHER['y']] = EMPTY_SPACE
    return boardCopy


def drawScore(score):
    scoreImg = BASICFONT.render(str(score), 1, SCORECOLOR)
    scoreRect = scoreImg.get_rect()
    scoreRect.bottomleft = (10, WINDOWHEIGHT - 6)
    DISPLAYSURF.blit(scoreImg, scoreRect)


if __name__ == '__main__':
    main()