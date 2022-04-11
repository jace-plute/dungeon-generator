import random as rd
import constants
import helperfuncs as hf

WALL_CHOICES = [constants.EMPTY_SPACE, constants.WALL]
VALID_WALL_POSITIONS = [constants.EMPTY_SPACE]
TRAP_CHOICES = [constants.EMPTY_SPACE, constants.TRAP]
TRAP_CHOICES_AT_SAFE_PATH = [constants.SAFE_PATH, constants.TRAP]
VALID_TRAP_POSITIONS = [constants.SAFE_PATH, constants.EMPTY_SPACE]
TRAP_POSITION_WEIGHTS = [1, 1.2]


def generateObstacles(width, height, map):
    # First, generate our walls.
    generateWalls(width, height, map)
    # Finish wall generation by filling in blocks surrounded on all valid sides with walls.
    fillInDeadSpace(width, height, map)

    # Next, generate traps.
    generateTraps(width, height, map)


def generateWalls(width, height, map):
    for i in range(width):
        for j in range(height):
            # Don't put a wall or an empty space over the safe path.
            # Additionally, verify we aren't going to lock in a cell in the middle of the map with walls and create a huge block of empty space.
            if map[i][j] in VALID_WALL_POSITIONS and verifyNoBlockage(i, j, map):
                map[i][j] = rd.choice(WALL_CHOICES)


def verifyNoBlockage(intendedWidthPos, intendedHeightPos, map):
    # Check surrounding cells and verify that there will not be a blockade.
    # Create a list of tuples of the positions to check.
    validPositions = hf.determineValidSurroundingPositions(
        intendedWidthPos, intendedHeightPos, map)

    countOfBlocks = 0
    for validWidth, validHeight in validPositions:
        if map[validWidth][validHeight] == constants.WALL:
            countOfBlocks += 1

    if countOfBlocks >= len(validPositions) - 1:
        return False
    else:
        return True


def fillInDeadSpace(width, height, map):
    # Because we are traversing the map (represented by a 2D array) from L->R, T->B,
    # we do run into a possibility of creating a blockade despite our best efforts.
    # That's okay - having sections of walls or "pillars" in an area could be fun.
    # So, if an EMPTY_SPACE is surrounded on all valid sides by WALLS, WALL in that EMPTY_SPACE.

    # This should trend towards the idea that every remaining empty space is a valid position to walk to.
    for i in range(width):
        for j in range(height):
            if not verifyNoBlockage(i, j, map):
                map[i][j] = constants.WALL


def generateTraps(width, height, map):
    # Traps should be slightly more likely to appear on the main path, so that
    # parties will run into some even if they follow the direct main path exclusively.
    for i in range(width):
        for j in range(height):
            if map[i][j] in VALID_TRAP_POSITIONS and map[i][j] == constants.SAFE_PATH:
                map[i][j] = rd.choices(
                    TRAP_CHOICES_AT_SAFE_PATH, TRAP_POSITION_WEIGHTS, k=1)[0]
            elif map[i][j] in VALID_TRAP_POSITIONS:
                map[i][j] = rd.choice(TRAP_CHOICES)
