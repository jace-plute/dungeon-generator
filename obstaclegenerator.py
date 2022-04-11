import constants
import helperfuncs as hf


def generateObstacles(width, height, map):

    pass


def verifyNoBlockage(intendedWidthPos, intendedHeightPos, map):
    # Check surrounding cells and verify that there will not be a blockade.
    # Create a list of tuples of the positions to check.
    validPositions = [(0, 0)]

    if hf.checkForOutOfBounds(intendedWidthPos - 1, intendedHeightPos, map):
        validPositions.append((intendedWidthPos - 1, intendedHeightPos))

    if hf.checkForOutOfBounds(intendedWidthPos + 1, intendedHeightPos, map):
        validPositions.append((intendedWidthPos + 1, intendedHeightPos))

    if hf.checkForOutOfBounds(intendedWidthPos, intendedHeightPos - 1, map):
        validPositions.append((intendedWidthPos, intendedHeightPos - 1))

    if hf.checkForOutOfBounds(intendedWidthPos, intendedHeightPos + 1, map):
        validPositions.append((intendedWidthPos, intendedHeightPos + 1))

    countOfBlocks = 0
    for validWidth, validHeight in validPositions:
        if map[validWidth][validHeight] == 1:
            countOfBlocks += 1

    if countOfBlocks >= 3:
        return False
    else:
        return True
