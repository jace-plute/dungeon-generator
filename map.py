import mapgenerator as mg


class Map:

    def __init__(self, width, height, entrancePosX, entrancePosY, goalPosX, goalPosY):
        self.width = width
        self.height = height
        self.entrancePosX = entrancePosX
        self.entrancePosY = entrancePosY
        self.goalPosX = goalPosX
        self.goalPosY = goalPosY

    def generateMap(self):
        self.map = mg.generateMap(self.width, self.height, self.entrancePosX,
                                  self.entrancePosY, self.goalPosX, self.goalPosY)
