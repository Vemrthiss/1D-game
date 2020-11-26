from assets.tiles.BoardTile import BoardTile

class Utility(BoardTile):
    def __init__(self, name):
        BoardTile.__init__(self, name)
        self.symbol = 'UTILITY'