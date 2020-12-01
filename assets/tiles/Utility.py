from assets.tiles.Property import Property

class Utility(Property):
    def __init__(self, name, listing_price):
        Property.__init__(self, name, listing_price)
        self.symbol = 'UTILITY'
        self.rental = 100 #dummy value, to be deleted for the one below later
        #self.rental = 4*dice_roll #IF OWNER HAS BOTH UTILTIES, IT WOULD BE 10X INSTEAD