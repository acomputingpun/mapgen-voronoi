import utils, vecs, pseudo, dirconst

class Tile():
    def __init__(self, grid, xyPos):
        self.grid = grid
        self.xyPos = vecs.Vec2(xyPos)
        self.dominantSource = None

    def closestSource(self):
        bestSource = utils.setPick(self.grid.regionSources)
        bestSourceDist = self.vDist(bestSource)
        for source in self.grid.regionSources:
            sourceDist = self.vDist(source)
            if sourceDist < bestSourceDist:
                bestSource = source
                bestSourceDist = sourceDist
        return bestSource
    def vDist(self, other):
        return self.grid.vDist(self, other)
    def closestSourceDist(self):
        return self.vDist(self.closestSource())

    def markDominantSource(self):
        self.dominantSource = self.closestSource()
        self.dominantSource.initialTiles.append(self)

    def adjacentTiles(self):
        for vec in dirconst.CARDINALS:
            adjPos = self.xyPos + vec
            if self.grid.containsPos( adjPos ):
                yield self.grid.lookup(adjPos)

    def isBorderTile(self):
        for adjTile in self.adjacentTiles():
            if adjTile.dominantSource is not self.dominantSource:
                return True
        return False

    def __repr__(self):
        return f"T {self.xyPos}"
