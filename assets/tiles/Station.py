from assets.tiles.Property import Property

class Station(Property):
    def __init__(self, name, listing_price):
        Property.__init__(self, name, listing_price)
        self.symbol = 'STATION'
        self.rental = .25*self.listing_price #hard-coded value