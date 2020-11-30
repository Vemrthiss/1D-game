num_tiles = 40

board_assets = { #defines how many of each tile type there should be in the board, TO BE REMOVED????
    'start': 1, #start/parking are corner pairs
    'parking': 1,
    'jail': 1, #jail tile is also 'just visiting' if he/she is not in jail
    'go_jail': 1, #jail/go_jail are corner pairs
    'chance': 3,
    'community_chest': 3,
    'small_tax': 1,
    'large_tax': 1,
    'train_station': 4, #one on each side
    'utility_bills': 2 #e.g. water, electricity
}

def get_max_tile_length():
    max_length = 0
    for key in board_assets: #references 'board_layout' variable of this file
        if len(key) > max_length:
            max_length = len(key)
    return max_length

max_tile_length = get_max_tile_length()

board_streets = [
    #harbourfront here (35)
    {'position': 37, 'name': 'Pasir Panjang', 'value': 750}, #D5
    {'position': 39, 'name': 'Tiong Bahru', 'value': 950}, #D3
    {'position': 1, 'name': 'Buona Vista', 'value': 750}, #D5
    {'position': 3, 'name': 'Jurong East', 'value': 525}, #D22
    #jurong west here (5)
    {'position': 6, 'name': 'Bukit Batok', 'value': 525}, #D23
    {'position': 8, 'name': 'Yew Tee', 'value': 525}, #D23 
    {'position': 9, 'name': 'Woodlands', 'value': 475}, #D27
    {'position': 11, 'name': 'Sembawang', 'value': 475}, #D27
    {'position': 13, 'name': 'Yishun', 'value': 475}, #D27
    {'position': 14, 'name': 'Ang Mo Kio', 'value': 800}, #D20
    #bishan here (15)
    {'position': 16, 'name': 'Toa Payoh', 'value': 700}, #D12
    {'position': 18, 'name': 'Potong Pasir', 'value': 800}, #D13
    {'position': 19, 'name': 'Serangoon', 'value': 700}, #D12
    {'position': 21, 'name': 'Sengkang', 'value': 625}, #D19
    {'position': 23, 'name': 'Punggol', 'value': 625}, #D19
    {'position': 24, 'name': 'Pasir Ris', 'value': 550}, #D18
    #bedok here (25)
    {'position': 26, 'name': 'Kembangan', 'value': 775}, #D14
    {'position': 27, 'name': 'Katong', 'value': 700}, #D15
    {'position': 29, 'name': 'Marine Parade', 'value': 700}, #D15
    {'position': 31, 'name': 'Geylang', 'value': 775}, #D14
    {'position': 32, 'name': 'Mountbatten', 'value': 700}, #d15
    {'position': 34, 'name': 'Tanjong Pagar', 'value': 1200} #D2
]