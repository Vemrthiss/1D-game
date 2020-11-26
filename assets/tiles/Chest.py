from assets.tiles.BoardTile import BoardTile

class Chest(BoardTile):
    def __init__(self):
        name = 'Community Chest'
        BoardTile.__init__(self, name)
        self.symbol = 'CHEST'