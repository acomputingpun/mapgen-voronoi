class RegionSource():
    def __init__(self, tile):
        self.tile = tile
        self.debugChar = self.grid.roller.choice("abcdefghijklmnopqrstuvwxyz")
        self.initialTiles = []

    @property
    def xyPos(self):
        return self.tile.xyPos
    @property
    def grid(self):
        return self.tile.grid

class Region():
    def __init__(self, initialTiles):
        self.tiles = set()
        self.borderTiles = set()
        self.innerTiles = set()

        for tile in initialTiles:
            self.tiles.add( tile )
        self.cleanupInitialTiles()

    def cleanupInitialTiles():
        contiguous = self.rTraverse(utils.setPick(self.tiles))
        for tile in (self.tiles - contiguous):
            raise Exception("Error: not yet inmplemented handling of noncontiguous regions")

        for tile in self.tiles:
            if tile.isBorderTile(self)
                self.borderTiles.add(tile)
            else:
                self.innerTiles.add(tile)

    def rTraverse(self, tile):
        return self._recursiveExpand(tile, set())
    def _rTraverse(self, cur, visited):
        if cur in self.tiles:
            if cur not in visited:
                visited.add(cur)
                for tile in cur.adjacentTiles():
                    self._rTraverse(tile, visited)
        return visited
