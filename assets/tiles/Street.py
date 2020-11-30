from assets.tiles.Property import Property

class Street(Property):
    def __init__(self, name, listing_price):
        Property.__init__(self, name, listing_price)
        self.symbol = 'STREET'
        self.rental = .5*self.listing_price #hard-coded value