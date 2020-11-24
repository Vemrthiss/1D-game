class Property():
    def __init__(self, name, location, value, rental):
        self.name = name
        self.location = location
        self.value = value
        self.rental = rental
        #initialise the initial "owner" as 0 (no player 0) on instantiation
        # will later have the player number attached to this owner property
        # owner attribute is useful to find out to whom the person landing on the current board has to pay
        self.owner = 0

    def assign_owner(self, player_no):
        self.owner = player_no

