from assets.tiles.BoardTile import BoardTile

class Station(BoardTile):
    def __init__(self, name):
        BoardTile.__init__(self, name)
        self.symbol = 'STATION'