

class Prov:
    def __init__(self):
        self.poses = set()

class Tile:
    def __init__(self, grid, xyPos):
        self.grid = grid
        self.xyPos = (self.xPos, self.yPos) = xyPos

class Grid:
    def __init__(self, xySize):
        self.xySize = (self.xSize, self.ySize) = xySize
        self._allTiles = { xyPos : Tile(self, xyPos) for xyPos in self.allPoses() }

    def lookup(self, xyPos):
        return self._allTiles[xyPos]

    def allTiles(self):
        yield from self._allTiles.values()

    def allPoses(self):
        for y in range(self.ySize):
            for x in range(self.xSize):
                yield (x, y)
