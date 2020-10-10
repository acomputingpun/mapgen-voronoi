import grids

vGrid = grids.VoronoiGrid( (30, 30), 10, (0, 1) )
vGrid.generate(10)
vGrid.debugPrint()
