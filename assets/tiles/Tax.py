from assets.tiles.BoardTile import BoardTile

class Tax(BoardTile):
    def __init__(self, typ):
        if typ == 'small':
            name = 'Road Tax'
            self.amount = 100
        elif typ == 'large':
            name = 'Income Tax'
        BoardTile.__init__(self, name)
        self.symbol = 'TAX'

    def determine_income_tax(self, player_obj):
        #player to pay minimum of 200 or 10% of his net worth, this sum should not be written as a self.amount attribute as it differs from player to player
        net_worth = player_obj.wallet
        amount_due = .1*net_worth
        if amount_due <= 200:
            amount_due = 200
        return amount_due