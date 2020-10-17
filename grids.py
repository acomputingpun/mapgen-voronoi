import utils, vecs, pseudo
import regions, tiles

class Grid():
    presetMinSourceDist = 2
    presetMinEdgeDist = 5

    def __init__(self, xySize, nRegions, wrapping = (0, 0)):
        self.xySize = vecs.Vec2(xySize)
        self.nRegions = nRegions
        self.wrapping = wrapping

    def clear(self):
        self._allTiles = { xyPos : tiles.Tile(self, xyPos) for xyPos in self.allPoses() }
        self.regionSources = []

    @property
    def xSize(self):
        return self.xySize.x
    @property
    def ySize(self):
        return self.xySize.y

    def xyWrap(self, xyPos):
        return vecs.Vec2( xyPos[0] % self.xySize.x if self.wrapping[0] else xyPos[0], xyPos[1] % self.xySize.y if self.wrapping[1] else xyPos[1] )

    def _containsWrappedPos(self, xyPos):
        return 0 <= xyPos.x < self.xySize.x and 0 <= xyPos.y < self.xySize.y
    def containsPos(self, xyPos):
        return self._containsWrappedPos(self.xyWrap(xyPos))

    def lookup(self, xyPos):
        return self._allTiles[self.xyWrap(xyPos)]

    def allTiles(self):
        yield from self._allTiles.values()

    def allPoses(self):
        for y in range(self.ySize):
            for x in range(self.xSize):
                yield vecs.Vec2(x, y)

    def pickRandomTiles(self, nTiles):
        randomTiles = []
        for k in range(nTiles):
            xyPos = vecs.Vec2(self.roller.randint(0, self.xSize), self.roller.randint(0, self.ySize))
            if (self.isValidRandomPos(xyPos)):
                randomTiles.append(self.lookup(xyPos))
        return randomTiles
    def isValidRandomPos(self, xyPos):
        if not (self.wrapping[0] or self.presetMinEdgeDist <= xyPos[0] < self.xySize[0]-self.presetMinEdgeDist):
            return False
        if not (self.wrapping[1] or self.presetMinEdgeDist <= xyPos[1] < self.xySize[1]-self.presetMinEdgeDist):
            return False
        return True

    def generate(self, seed):
        raise Exception ("To be overridden!")

class VoronoiGrid(Grid):
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
        randomTiles = self.pickRandomTiles(24)
        try:
            bestTile = utils.setPick(randomTiles)
            bestDist = bestTile.closestSourceDist()
            for tile in randomTiles:
                tileDist = tile.closestSourceDist()
                if tileDist > bestDist:
                    bestTile = tile
                    bestDist = tileDist
            if bestDist >= self.presetMinSourceDist:
                self.placeRegionSource(bestTile)
        except StopIteration:
            self.placeRegionSource(utils.setPick(randomTiles))

    def placeRegionSource(self, tile):
        self.regionSources.append(regions.RegionSource(tile))
