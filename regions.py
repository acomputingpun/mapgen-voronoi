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
