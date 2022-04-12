def checkForOutOfBounds(intendedWidthPos, intendedHeightPos, baseMap):
    # Check the positions around the intended x and y for OOB.
    # Also make sure we aren't negatively indexing the array - this will cause unintended behavior in the random walk.
    if(intendedWidthPos < 0 or intendedHeightPos < 0):
        return False

    try:
        baseMap[intendedWidthPos][intendedHeightPos]
    except:
        return False
    else:
        return True


def determineValidSurroundingPositions(intendedWidthPos, intendedHeightPos, map):
    validPositions = [(0, 0)]

    if checkForOutOfBounds(intendedWidthPos - 1, intendedHeightPos, map):
        validPositions.append((intendedWidthPos - 1, intendedHeightPos))

    if checkForOutOfBounds(intendedWidthPos + 1, intendedHeightPos, map):
        validPositions.append((intendedWidthPos + 1, intendedHeightPos))

    if checkForOutOfBounds(intendedWidthPos, intendedHeightPos - 1, map):
        validPositions.append((intendedWidthPos, intendedHeightPos - 1))

    if checkForOutOfBounds(intendedWidthPos, intendedHeightPos + 1, map):
        validPositions.append((intendedWidthPos, intendedHeightPos + 1))

    return validPositions
