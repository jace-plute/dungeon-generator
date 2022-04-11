import numpy as np
import pathgenerator as pg
import obstaclegenerator as og


def generateMapShape(width, height):
    # Create and return an empty structure representing the map.
    baseMap = np.array([[0] * height] * width)
    return baseMap


def generateMap(width, height, startPosX, startPosY, goalPosX, goalPosY):
    # Create the base map shape in the specified dimensions.
    map = generateMapShape(width, height)
    # Generate a baseline path from the specified entrance to the specified exit.
    # This ensures that we will not block the path from start to end when we do obstacle/wall generation.
    pg.defineStartAndEndAndGeneratePath(
        startPosX, startPosY, goalPosX, goalPosY, map)

    og.generateObstacles(width, height, map)

    return map
