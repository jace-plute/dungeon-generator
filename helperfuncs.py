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
