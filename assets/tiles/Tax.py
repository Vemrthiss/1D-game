from assets.tiles.BoardTile import BoardTile

class Tax(BoardTile):
    def __init__(self, typ):
        if typ == 'small':
            name = 'Road Tax'
            self.amount = 100
        elif typ == 'large':
            name = 'Income Tax'
            self.amount = 200
        BoardTile.__init__(self, name)
        self.symbol = 'TAX'
        