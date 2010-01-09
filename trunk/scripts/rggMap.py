'''
rggMap - for the Random Game Generator project            

By Doctus (kirikayuumura.noir@gmail.com)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
'''
import sys
import rggTile, rggPog, rggSystem, random
from rggJson import loadString, loadInteger, loadObject, loadArray, loadCoordinates

class Map(object):
    
    def __init__(self, mapname, authorname, mapsize, tileset, tilesize):
        """Initializes a new map."""
        
        self.ID = None
        self.mapname = mapname
        self.authorname = authorname
        self.mapsize = mapsize
        self.tileset = tileset
        self.tilesize = tilesize
        
        self.Pogs = {}
        self.tileindexes = [0 for i in xrange(mapsize[0] * mapsize[1])]
        self.hidden = True
        self.tiles = None
        
    def addPog(self, pog):
        """Adds a pog to the map, assigning it a unique id."""
        assert(pog.ID is not None)
        #if pog.ID is None:
        #    pog.ID = self._findUniqueID()
        if pog.ID in self.Pogs:
            self.Pogs[pog.ID].hide()
        self.Pogs[pog.ID] = pog
        if self.hidden:
            pog.hide()
        else:
            pog.show()
    
    def _findUniqueID(self, src):
        """Get a unique id for a pog."""
        id = src or rggSystem.findRandomAppend()
        while id in self.Pogs:
            id += rggSystem.findRandomAppend()
        return id
    
    def hide(self, hidden=True, includeTiles=True, includePogs=True):
        """Hide or show all pogs and tiles."""
        if hidden == self.hidden:
            return
        self.hidden = hidden
        if includePogs:
            if hidden:
                for pog in self.Pogs.values():
                    pog.hide()
            else:
                for pog in self.Pogs.values():
                    pog.show()
        if includeTiles:
            if hidden:
                self._deleteTiles()
            else:
                self._createTiles()
    
    def show(self):
        return self.hide(False)
    
    def _deleteTiles(self):
        for tile in self.tiles:
            tile.destroy()
        self.tiles = None
    
    def _createTiles(self):
        """Show all the tiles of this map."""
        self.tiles = []
        for y in xrange(0, self.mapsize[1]):
            for x in xrange(0, self.mapsize[0]):
                self.tiles.append(rggTile.tile(
                    (x * self.tilesize[0], y * self.tilesize[1]),
                    self.tilesize,
                    self.tileindexes[len(self.tiles)],
                    0,
                    self.tileset))
    
    def getTile(self, tile):
        """Change the specified tile."""
        x, y = tile
        assert(0 <= x <= self.mapsize[0])
        assert(0 <= y <= self.mapsize[1])
        t = x + self.mapsize[0] * y
        return self.tileindexes[t]
    
    def setTile(self, tile, index):
        """Change the specified tile."""
        x, y = tile
        assert(0 <= x <= self.mapsize[0])
        assert(0 <= y <= self.mapsize[1])
        t = x + self.mapsize[0] * y
        self.tileindexes[t] = index
        if not self.hidden:
            self.tiles[t].setTile(self.tileindexes[t])
    
    def _setIndexes(self, indexes):
        if len(indexes) != len(self.tileindexes):
            return
        self.tileindexes[:] = indexes[:]
        if not self.hidden:
            for i in xrange(len(indexes)):
                self.tiles[i].setTile(self.tileindexes[i])
                #print self.tileindexes[i], self.tiles[i].getTile()
    
    def findTopPog(self, position):
        """Returns the top pog at a given position, or None."""
        layer = -sys.maxint
        top = None
        for pog in self.Pogs.values():
            if layer >= pog.layer:
                continue
            if pog.pointCollides(position):
                top = pog
                layer = top.layer
        return top
    
    def dump(self):
        """Serialize to an object valid for JSON dumping."""
        thickOne = rggSystem.getLinesOfThickness(1)
        thickTwo = rggSystem.getLinesOfThickness(2)
        thickThree = rggSystem.getLinesOfThickness(3)

        tlines = [(line.x(), line.y(), line.width(), line.height(), 1) for line in thickOne]
        tlines.extend([(line.x(), line.y(), line.width(), line.height(), 2) for line in thickTwo])
        tlines.extend([(line.x(), line.y(), line.width(), line.height(), 3) for line in thickThree])

        return dict(
            mapname=self.mapname,
            authorname=self.authorname,
            mapsize=self.mapsize,
            tileset=self.tileset,
            tilesize=self.tilesize,
            pogs=dict([(pog.ID, pog.dump()) for pog in self.Pogs.values()]),
            tiles=self.tileindexes,
            #lines1=[(line.x(), line.y(), line.width(), line.height(), 1) for line in thickOne],
            #lines2=[(line.x(), line.y(), line.width(), line.height(), 2) for line in thickTwo],
            #lines3=[(line.x(), line.y(), line.width(), line.height(), 3) for line in thickThree])
            lines=tlines)
    
    @staticmethod
    def load(obj):
        """Deserialize a new map from a dictionary."""
        map = Map(
            loadString('Map.mapname', obj.get('mapname')),
            loadString('Map.authorname', obj.get('authorname')),
            loadCoordinates('Map.mapsize', obj.get('mapsize'), length=2, min=1, max=65535),
            loadString('Map.tileset', obj.get('tileset')),
            loadCoordinates('Map.tilesize', obj.get('tilesize'), length=2, min=1, max=65535))
        
        pogs = loadObject('Map.pogs', obj.get('pogs'))
        for ID, pog in pogs.items():
            loaded = rggPog.Pog.load(pog)
            loaded.ID = ID
            map.addPog(loaded)

        #lines = loadCoordinates('Map.lines', obj.get('lines'), length=5)
        #print lines
        #for x, y, w, h, t in lines:
        #    rggSystem.drawLine(x, y, w, h, t)
        
        # HACK: Looks like coordinates; saves work.
        tiles = loadCoordinates('Map.tiles', obj.get('tiles'), length=len(map.tileindexes), min=0, max=65535)
        map._setIndexes(tiles)
        return map
        
    def __unicode__(self):
        return "{0} {1}".format(self.mapname, self.ID)
    
    def __str__(self):
        return self.__unicode__()
