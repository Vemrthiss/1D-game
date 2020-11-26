from assets.tiles.BoardTile import BoardTile

class Tax(BoardTile):
    def __init__(self, typ):
        name = 'Road Tax' if typ == 'small' else 'Income Tax'
        BoardTile.__init__(self, name)
        self.symbol = 'TAX'
        