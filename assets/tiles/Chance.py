from assets.tiles.BoardTile import BoardTile

class Chance(BoardTile):
    def __init__(self):
        name = 'Chance?'
        BoardTile.__init__(self, name)
        self.symbol = 'CHANCE'