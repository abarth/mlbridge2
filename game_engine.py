SUITS = [ "C", "D", "H", "S" ]
RANKS = [ "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" ]
CARDS = [ f"{rank}{suit}" for suit in SUITS for rank in RANKS ]

STRAINS = SUITS + [ "NT" ]
CALLS = [ "P", "X", "XX" ] + [ f"{level + 1}{strain}" for level in range(7) for strain in STRAINS ]

POSITIONS = [ "N", "E", "S", "W" ]
VULNERABILITIES = [ "E-W", "N-S", "None", "Both" ]

def get_vulnerability_from_board_number(board_number):
    board_number_to_vulnerability = {
        0: 'E-W', # board 16
        1: 'None',
        2: 'N-S',
        3: 'E-W',
        4: 'Both',
        5: 'N-S',
        6: 'E-W',
        7: 'Both',
        8: 'None',
        9: 'E-W',
        10: 'Both',
        11: 'None',
        12: 'N-S',
        13: 'Both',
        14: 'None',
        15: 'N-S',
    }
    return board_number_to_vulnerability[board_number % 16]

def get_dealer_from_board_number(board_number):
    return POSITIONS[board_number % 4]

def get_hands_from_identifier(identifier):
    hands = [[] for p in POSITIONS]
    hexChars = '0123456789abcdef'
    for charIndex, hexChar in enumerate(identifier):
        hexIndex = hexChars.index(hexChar)
        highHandIndex = hexIndex // 4
        lowHandIndex = hexIndex - highHandIndex * 4
        highCard = CARDS[charIndex * 2 + 0]
        lowCard = CARDS[charIndex * 2 + 1]
        hands[highHandIndex].append(highCard)
        hands[lowHandIndex].append(lowCard)
    return {POSITIONS[i]: hands[i] for i in range(len(hands))}

def get_board_from_identifier(identifier):
    components = identifier.split("-")
    assert(len(components) == 2)
    board_number_string, deal_identifier = components
    board_number = int(board_number_string)
    return {
        "dealer": get_dealer_from_board_number(board_number),
        "vulnerability": get_vulnerability_from_board_number(board_number),
        "hands": get_hands_from_identifier(deal_identifier),
    }
