class Property():
    def __init__(self, name, location, value, rental):
        self.name = name
        self.location = location
        self.value = value
        self.rental = rental
        #initialise an empty string on instantiation but should hold a player_no to reflect current owner
        # owner attribute is useful to find out to whom the person landing on the current board has to pay
        self.owner = ''

    def assign_owner(self, player_no):
        self.owner = player_no

