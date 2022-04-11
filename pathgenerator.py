import constants
import random as rd
import helperfuncs as hf

GOAL_X = 0
GOAL_Y = 0


def defineStartAndEndAndGeneratePath(startPosX, startPosY, endPosX, endPosY, baseMap):
    global GOAL_X
    GOAL_X = endPosX
    global GOAL_Y
    GOAL_Y = endPosY
    baseMap[startPosX][startPosY] = constants.START
    baseMap[endPosX][endPosY] = constants.END

    generatePathRecursive(startPosX, startPosY, startPosX, startPosY, baseMap)


def generatePath(currentPosX, currentPosY, baseMap):
    directions = ['up', 'down', 'left', 'right']
    foundExit = False

    while not foundExit:
        step = rd.choice(directions)
        # Try the random step
        if step == 'up':
            if hf.checkForOutOfBounds(currentPosX, currentPosY - 1, baseMap):
                currentPosY -= 1
            else:
                continue
        elif step == 'down':
            if hf.checkForOutOfBounds(currentPosX, currentPosY + 1, baseMap):
                currentPosY += 1
            else:
                continue
        elif step == 'left':
            if hf.checkForOutOfBounds(currentPosX - 1, currentPosY, baseMap):
                currentPosX -= 1
            else:
                continue
        else:
            if hf.checkForOutOfBounds(currentPosX + 1, currentPosY, baseMap):
                currentPosX += 1
            else:
                continue

        # If we didn't hit a continue block, we verified the bounds and updated current positions.
        # Verify that the space we are at is not the exit - if it is the exit, let's leave the loop.
        if baseMap[currentPosX][currentPosY] == constants.END:
            foundExit = True
        # Don't accidentally mark over the entrance
        elif baseMap[currentPosX][currentPosY] == constants.START:
            continue
        # Assign a path mark
        else:
            baseMap[currentPosX][currentPosY] = constants.SAFE_PATH


def generatePathRecursive(currentPosX, currentPosY, previousPosX, previousPosY, baseMap):
    tempPosX = currentPosX
    tempPosY = currentPosY

    step = generateStep(currentPosX, currentPosY,
                        previousPosX, previousPosY, baseMap)
    currentPosX = step[0]
    currentPosY = step[1]

    # Verify that the space we are at is not the exit - if it is the exit, end recursion.
    if baseMap[currentPosX][currentPosY] == constants.END:
        return
    # Don't accidentally mark over the entrance
    elif baseMap[currentPosX][currentPosY] == constants.START:
        pass
    # Assign a path mark
    else:
        baseMap[currentPosX][currentPosY] = constants.SAFE_PATH

    generatePathRecursive(currentPosX, currentPosY,
                          tempPosX, tempPosY, baseMap)


def generateStep(currentPosX, currentPosY,  previousPosX, previousPosY, baseMap):
    # Weight needs to be associated to each direction from the current position - this is so that we trend towards moving closer to the goal, but also
    # allow for deviations from the shortest path.
    # Once we determine weights, we need to return the random function's result to the caller, so it can make the step.
    possiblePositions = []
    weights = []

    # The maximum possible steps we could take is the dimensions of the 2D array - 1. We will back scale the
    # weights based on steps, so substract steps from maximumStep to determine the weight.
    maximumStep = len(baseMap) + len(baseMap[0])

    if hf.checkForOutOfBounds(currentPosX, currentPosY - 1, baseMap):
        possiblePositions.append((currentPosX, currentPosY - 1))
    if hf.checkForOutOfBounds(currentPosX, currentPosY + 1, baseMap):
        possiblePositions.append((currentPosX, currentPosY + 1))
    if hf.checkForOutOfBounds(currentPosX - 1, currentPosY, baseMap):
        possiblePositions.append((currentPosX - 1, currentPosY))
    if hf.checkForOutOfBounds(currentPosX + 1, currentPosY, baseMap):
        possiblePositions.append((currentPosX + 1, currentPosY))

    # Remove backtracking to prevent stack overflow by calling recursive function.
    if (previousPosX, previousPosY) in possiblePositions:
        possiblePositions.remove((previousPosX, previousPosY))

    stepsFromGoal = []
    for positionX, positionY in possiblePositions:
        stepsFromGoal.append(abs(GOAL_X - positionX) + abs(GOAL_Y - positionY))

    for steps in stepsFromGoal:
        weights.append((maximumStep - steps) ** 2)

    return rd.choices(possiblePositions, k=1, weights=weights)[0]
