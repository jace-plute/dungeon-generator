import random as rd
import numpy as np
import constants
import helperfuncs as hf
import pathgenerator as pg


def generateMapShape(width, height):
    # Create and return an empty structure representing the map.
    baseMap = np.array([[0] * height] * width)
    #baseMap = np.random.randint(0, 2, size=(width, height))
    return baseMap


def generateNoise(width, height, baseMap):
    # Remove obstacles if there is a complete blockage.
    for i in range(width):
        for j in range(height):
            if not verifyNoBlockage(i, j, baseMap):
                baseMap[i][j] = 0

    return baseMap


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


def generateMap(width, height):
    map = generateMapShape(width, height)
    pg.defineStartAndEndAndGeneratePath(0, 0, 9, 9, map)

    #map = generateNoise(width, height, map)

    return map


print(generateMap(10, 10))
