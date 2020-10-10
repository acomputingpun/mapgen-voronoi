import grids, webs

vGrid = grids.VoronoiGrid( (30, 30), 10, (0, 1) )
vGrid.generate(10)

vWeb = webs.Web(vGrid)
vWeb.debugPrint()
