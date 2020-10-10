import utils, vecs, pseudo

class RegionSource():
    def __init__(self, tile):
        self.tile

    @property
    def xyPos(self):
        return self.tile.xyPos
    @property
    def grid(self):
        return self.tile.grid


class Region():
    def __init__(self, source):
        self.poses = set()

class Tile():
    def __init__(self, grid, xyPos):
        self.grid = grid
        self.xyPos = vecs.Vec2(xyPos)

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
        return self.parent.vDist(self, other)
    def closestSourceDist(self):
        return self.vDist(self.closestSource())

class Grid():
    def __init__(self, xySize, nRegions):
        self.xySize = vecs.Vec2(xySize)
        self.nRegions = nRegions
        self.roller = None

    def clear(self):
        self._allTiles = { xyPos : Tile(self, xyPos) for xyPos in self.allPoses() }
        self.regionSources = []
        self.regions = []

    def lookup(self, xyPos):
        return self._allTiles[xyPos]

    def allTiles(self):
        yield from self._allTiles.values()

    def allPoses(self):
        for y in range(self.xySize.y):
            for x in range(self.xySize.x):
                yield Vecs.vec2(x, y)

    def pickRandomTiles(self, nTiles):
        randomTiles = set([])
        for k in range(nTiles):
            xyPos = (self.roller.randint(0, self.xySize.x), self.roller.randint(0, self.xySize.y))
            randomTiles.add(self.lookup(xyPos))
        return randomTiles

    def generate(self, seed):
        raise Exception ("To be overridden!")

class VoronoiGrid(Grid):
    def generate(self, seed = 0):
        self.clear()
        self.roller = pseudo.Roller(seed)

        while len(self.regionSources) < self.nRegions:
            self.rPlaceRegionSource()

    @staticmethod
    def vDist(item1, item2):
        return item1.xyPos.dist(item2.xyPos)

    def rPlaceRegionSource(self):
        randomTiles = self.pickRandomTiles()
        bestTile = utils.setPick(randomTiles)
        bestDist = bestTile.closestSourceDist()
        for tile in randomTiles:
            tileDist = tile.closestSourceDist()
            if tile.vDist(closestSource) < bestDist:
                bestTile = tile
                bestDist = tileDist
        self.placeRegionSource(bestTile)

    def placeRegionSource(self, tile):
        self.regionSources.append(RegionSource(self, tile))
