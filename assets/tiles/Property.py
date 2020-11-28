from assets.tiles.BoardTile import BoardTile

class Property(BoardTile):
    def __init__(self, name, listing_price):
        BoardTile.__init__(self, name)
        self.listing_price = listing_price
        self.owner = 0
        #self.rental and self.symbol to be set in child classes
    
    def update_owner(self, player_no):
        self.owner = player_no