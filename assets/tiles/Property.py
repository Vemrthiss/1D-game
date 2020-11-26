from assets.tiles.BoardTile import BoardTile

class Property(BoardTile):
    def __init__(self, name):
        BoardTile.__init__(self, name)
        self.symbol = 'PROPERTY'