from assets.tiles.BoardTile import BoardTile

class Start(BoardTile):
    def __init__(self):
        name = 'GO'
        BoardTile.__init__(self, name)
        self.symbol = 'START'

class Parking(BoardTile):
    def __init__(self):
        name = 'Free Parking'
        BoardTile.__init__(self, name)
        self.symbol = 'PARKING'

class Jail(BoardTile):
    def __init__(self):
        name = 'In Jail/Just Visiting'
        BoardTile.__init__(self, name)
        self.symbol = 'JAIL'

class GoJail(BoardTile):
    def __init__(self):
        name ='Go To Jail'
        BoardTile.__init__(self, name)
        self.symbol = 'GO_JAIL'