import regions

class Web():
    def __init__(self, grid):
        self.grid = grid
        self.regions = []
        self.processInitialGrid()

    @property
    def regionSources(self):
        return self.grid.regionSources

    def lookup(self, xyPos):
        return self.grid.lookup(xyPos)

    def processInitialGrid(self):
        for source in self.regionSources:
            self.regions.append(regions.Region(source))

    def debugPrint(self):
        for y in range(self.grid.ySize):
            for x in range(self.grid.xSize):
                tile = self.lookup((x, y))
                rSource = tile.dominantSource
                if rSource.tile == tile:
                    print(rSource.debugChar.upper(), end='')
                else:
                    print(rSource.debugChar, end='')
            print()
