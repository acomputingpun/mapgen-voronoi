import utils

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
    def __init__(self, source):
        self.source = source

        self.tiles = set()
        self.borderTiles = set()
        self.innerTiles = set()

        for tile in source.initialTiles:
            self.tiles.add( tile )
        self.cleanupInitialTiles()

    def cleanupInitialTiles(self):
        contiguous = self.rTraverse(utils.setPick(self.tiles))
        for tile in (self.tiles - contiguous):
            raise Exception("Error: not yet inmplemented handling of noncontiguous regions")

        for tile in self.tiles:
            if tile.isBorderTile():
                self.borderTiles.add(tile)
            else:
                self.innerTiles.add(tile)

    def rTraverse(self, tile):
        return self._rTraverse(tile, set())
    def _rTraverse(self, cur, visited):
        if cur in self.tiles:
            if cur not in visited:
                visited.add(cur)
                for tile in cur.adjacentTiles():
                    self._rTraverse(tile, visited)
        return visited

    @property
    def adjRegions(self):
        try:
            if self._adjRegions_dirty:
                self._adjRegions_cached = self._adjRegions()
                self._adjRegions_dirty = False
            return self._adjRegions_cached
        except AttributeError:
            self._adjRegions_cached = self._adjRegions()
            self._adjRegions_dirty = False
            return self.adjRegions

    def _adjRegions(self):
        adjRegions = set()
        for tile in self.borderTiles:
            adjRegions.add(tile)
        return adjRegions
