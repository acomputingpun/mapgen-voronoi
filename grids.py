import utils, vecs, pseudo

class RegionSource():
    def __init__(self, tile):
        self.tile = tile
        self.debugChar = self.grid.roller.choice("abcdefghijklmnopqrstuvwxyz")

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

class Grid():
    roller = None

    def __init__(self, xySize, nRegions, wrapping = (0, 0)):
        self.xySize = vecs.Vec2(xySize)
        self.nRegions = nRegions
        self.wrapping = wrapping

    def clear(self):
        self._allTiles = { xyPos : Tile(self, xyPos) for xyPos in self.allPoses() }
        self.regionSources = []
        self.regions = []

    @property
    def xSize(self):
        return self.xySize.x
    @property
    def ySize(self):
        return self.xySize.y

    def lookup(self, xyPos):
        return self._allTiles[xyPos]

    def allTiles(self):
        yield from self._allTiles.values()

    def allPoses(self):
        for y in range(self.ySize):
            for x in range(self.xSize):
                yield vecs.Vec2(x, y)

    def pickRandomTiles(self, nTiles):
        randomTiles = set([])
        for k in range(nTiles):
            xyPos = (self.roller.randint(0, self.xSize), self.roller.randint(0, self.ySize))
            randomTiles.add(self.lookup(xyPos))
        return randomTiles

    def generate(self, seed):
        raise Exception ("To be overridden!")

class VoronoiGrid(Grid):
    presetMinDist = 2

    def generate(self, seed = 0):
        self.clear()
        self.roller = pseudo.Roller(seed)

        while len(self.regionSources) < self.nRegions:
            self.rPlaceRegionSource()

        for tile in self.allTiles():
            tile.markDominantSource()

    def debugPrint(self):
        for y in range(self.ySize):
            for x in range(self.xSize):
                print(self.lookup((x, y)).dominantSource.debugChar, end='')
            print()

    def vDist(self, item1, item2):
        xDist = abs(item1.xyPos.x - item2.xyPos.x)
        yDist = abs(item1.xyPos.y - item2.xyPos.y)

        if self.wrapping[0]:
            xDist = min(xDist, self.xSize-xDist)
        if self.wrapping[1]:
            yDist = min(yDist, self.ySize-yDist)
        return vecs.Vec2(xDist, yDist).mag

    def rPlaceRegionSource(self):
        try:
            randomTiles = self.pickRandomTiles(24)
            bestTile = utils.setPick(randomTiles)
            bestDist = bestTile.closestSourceDist()
            for tile in randomTiles:
                tileDist = tile.closestSourceDist()
                if tileDist > bestDist:
                    bestTile = tile
                    bestDist = tileDist
            if bestDist >= self.presetMinDist:
                self.placeRegionSource(bestTile)
        except StopIteration:
            self.placeRegionSource(utils.setPick(self.allTiles()))

    def placeRegionSource(self, tile):
        self.regionSources.append(RegionSource(tile))
