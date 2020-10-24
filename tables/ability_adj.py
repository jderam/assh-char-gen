adj_descriptions = {
    'STR': {
        'short': [
            'Atk Mod',
            'Dmg Adj',
            'Test',
            'Feat',
        ],
        'long': [
            'Melee Attack',
            'Damage Adjustment',
            'Test of STR',
            'Feat of STR',
        ],
    },
    'DEX': {
        'short': [
            'Atk Mod',
            'Def Adj',
            'Test',
            'Feat',
        ],
        'long': [
            'Missile Attack',
            'Defense Adjustment',
            'Test of DEX',
            'Feat of DEX',
        ],
    },
    'CON': {
        'short': [
            'HP Adj',
            'Poison Adj',
            'Surv',
            'Test',
            'Feat',
        ],
        'long': [
            'Hit Point Adjustment',
            'Poison Adjustment',
            'Trauma Survival',
            'Test of CON',
            'Feat of CON',
        ],
    },
    'INT': {
        'short': [
            'Lang',
            'Bonus Spells',
            'Learn Spell',
        ],
        'long': [
            'Languages',
            'Bonus Spells Per Day',
            'Chance to Learn Spell',
        ],
    },
    'WIS': {
        'short': [
            'Will Adj',
            'Bonus Spells',
            'Learn Spell',
        ],
        'long': [
            'Willpower Adjustment',
            'Bonus Spells Per Day',
            'Chance to Learn Spell',
        ],
    },
    'CHA': {
        'short': [
            'Reac Adj',
            'Max Henchmen',
            'Turning Adj',
        ],
        'long': [
            'Reaction / Loyalty Adjustment',
            'Maximum Number of Henchmen',
            'Undead Turning Adjustment',
        ],
    },
}

# str_adj_desc = [
#     ("Melee Attack", "Atk Mod"),
#     ("Damage Adjustment", "Dmg Adj"),
#     ("Test of STR", "Test"),
#     ("Feat of STR", "Feat"),
# ]

# dex_adj_desc = [
#     ("Missile Attack", "Atk Mod"),
#     ("Defense Adjustment", "Def Adj"),
#     ("Test of DEX", "Test"),
#     ("Feat of DEX", "Feat"),
# ]

# con_adj_desc = [
#     ("Hit Point Adjustment", "HP Adj"),
#     ("Poison Adjustment", "Poison Adj"),
#     ("Trauma Survival", "Surv"),
#     ("Test of CON", "Test"),
#     ("Feat of CON", "Feat"),
# ]

# int_adj_desc = [
#     ("Languages", "Lang"),
#     ("Bonus Spells Per Day", "Bonus Spells"),
#     ("Chance to Learn Spell", "Learn Spell"),
# ]

# wis_adj_desc = [
#     ("Willpower Adjustment", "Will Adj"),
#     ("Bonus Spells Per Day", "Bonus Spells"),
#     ("Chance to Learn Spell", "Learn Spell"),
# ]

# cha_adj_desc = [
#     ("Reaction / Loyalty Adjustment", "Reac Adj"),
#     ("Maximum Number of Henchmen", "Max Henchmen"),
#     ("Undead Turning Adjustment", "Turning Adj"),
# ]

adjustments = {
    'STR': {
        3:  [-2, -2, "1:6", "0%"],
        4:  [-1, -1, "1:6", "1%"],
        5:  [-1, -1, "1:6", "1%"],
        6:  [-1, -1, "1:6", "1%"],
        7:  [ 0, -1, "2:6", "2%"],
        8:  [ 0, -1, "2:6", "2%"],
        9:  [ 0,  0, "2:6", "4%"],
        10: [ 0,  0, "2:6", "4%"],
        11: [ 0,  0, "2:6", "4%"],
        12: [ 0,  0, "2:6", "4%"],
        13: [ 0,  1, "3:6", "8%"],
        14: [ 0,  1, "3:6", "8%"],
        15: [ 1,  1, "3:6", "16%"],
        16: [ 1,  1, "3:6", "16%"],
        17: [ 1,  2, "4:6", "24%"],
        18: [ 2,  3, "5:6", "32%"],
    },
    'DEX': {
        3:  [-2, -2, "1:6", "0%"],
        4:  [-1, -1, "1:6", "1%"],
        5:  [-1, -1, "1:6", "1%"],
        6:  [-1, -1, "1:6", "1%"],
        7:  [-1,  0, "2:6", "2%"],
        8:  [-1,  0, "2:6", "2%"],
        9:  [ 0,  0, "2:6", "4%"],
        10: [ 0,  0, "2:6", "4%"],
        11: [ 0,  0, "2:6", "4%"],
        12: [ 0,  0, "2:6", "4%"],
        13: [ 1,  0, "3:6", "8%"],
        14: [ 1,  0, "3:6", "8%"],
        15: [ 1,  1, "3:6", "16%"],
        16: [ 1,  1, "3:6", "16%"],
        17: [ 2,  1, "4:6", "24%"],
        18: [ 3,  2, "5:6", "32%"],
    },
    'CON': {
        3:  [-1, -2, "45%", "1:6", "0%"],
        4:  [-1, -1, "55%", "1:6", "1%"],
        5:  [-1, -1, "55%", "1:6", "1%"],
        6:  [-1, -1, "55%", "1:6", "1%"],
        7:  [ 0,  0, "65%", "2:6", "2%"],
        8:  [ 0,  0, "65%", "2:6", "2%"],
        9:  [ 0,  0, "75%", "2:6", "4%"],
        10: [ 0,  0, "75%", "2:6", "4%"],
        11: [ 0,  0, "75%", "2:6", "4%"],
        12: [ 0,  0, "75%", "2:6", "4%"],
        13: [ 1,  0, "80%", "3:6", "8%"],
        14: [ 1,  0, "80%", "3:6", "8%"],
        15: [ 1,  1, "85%", "3:6", "16%"],
        16: [ 1,  1, "85%", "3:6", "16%"],
        17: [ 2,  1, "90%", "4:6", "24%"],
        18: [ 3,  2, "95%", "5:6", "32%"],
    },
    'INT': {
        3:  ["Illiterate", "N/A", "N/A"],
        4:  ["Illiterate", "N/A", "N/A"],
        5:  ["Illiterate", "N/A", "N/A"],
        6:  ["Illiterate", "N/A", "N/A"],
        7:  ["+0", "N/A", "N/A"],
        8:  ["+0", "N/A", "N/A"],
        9:  ["+0", "--", "50%"],
        10: ["+0", "--", "50%"],
        11: ["+0", "--", "50%"],
        12: ["+0", "--", "50%"],
        13: ["+1", "1st", "65%"],
        14: ["+1", "1st", "65%"],
        15: ["+1", "1st, 2nd", "75%"],
        16: ["+1", "1st, 2nd", "75%"],
        17: ["+2", "1st, 2nd, 3rd", "85%"],
        18: ["+3", "1st, 2nd, 3rd, 4th", "95%"],
    },
    'WIS': {
        3:  [-2, "N/A", "N/A"],
        4:  [-1, "N/A", "N/A"],
        5:  [-1, "N/A", "N/A"],
        6:  [-1, "N/A", "N/A"],
        7:  [0, "N/A", "N/A"],
        8:  [0, "N/A", "N/A"],
        9:  [0, "--", "50%"],
        10: [0, "--", "50%"],
        11: [0, "--", "50%"],
        12: [0, "--", "50%"],
        13: [0, "1st", "65%"],
        14: [0, "1st", "65%"],
        15: [1, "1st, 2nd", "75%"],
        16: [1, "1st, 2nd", "75%"],
        17: [1, "1st, 2nd, 3rd", "85%"],
        18: [2, "1st, 2nd, 3rd, 4th", "95%"],
    },
    'CHA': {
        3:  [-3,  1, -1],
        4:  [-2,  2, -1],
        5:  [-2,  2, -1],
        6:  [-2,  2, -1],
        7:  [-1,  3,  0],
        8:  [-1,  3,  0],
        9:  [ 0,  4,  0],
        10: [ 0,  4,  0],
        11: [ 0,  4,  0],
        12: [ 0,  4,  0],
        13: [ 1,  6,  0],
        14: [ 1,  6,  0],
        15: [ 1,  8,  1],
        16: [ 1,  8,  1],
        17: [ 2, 10,  1],
        18: [ 3, 12,  1],
    },
}

# str_adj = {
#     3:  [-2, -2, "1:6", "0%"],
#     4:  [-1, -1, "1:6", "1%"],
#     5:  [-1, -1, "1:6", "1%"],
#     6:  [-1, -1, "1:6", "1%"],
#     7:  [ 0, -1, "2:6", "2%"],
#     8:  [ 0, -1, "2:6", "2%"],
#     9:  [ 0,  0, "2:6", "4%"],
#     10: [ 0,  0, "2:6", "4%"],
#     11: [ 0,  0, "2:6", "4%"],
#     12: [ 0,  0, "2:6", "4%"],
#     13: [ 0,  1, "3:6", "8%"],
#     14: [ 0,  1, "3:6", "8%"],
#     15: [ 1,  1, "3:6", "16%"],
#     16: [ 1,  1, "3:6", "16%"],
#     17: [ 1,  2, "4:6", "24%"],
#     18: [ 2,  3, "5:6", "32%"],
# }

# dex_adj = {
#     3:  [-2, -2, "1:6", "0%"],
#     4:  [-1, -1, "1:6", "1%"],
#     5:  [-1, -1, "1:6", "1%"],
#     6:  [-1, -1, "1:6", "1%"],
#     7:  [-1,  0, "2:6", "2%"],
#     8:  [-1,  0, "2:6", "2%"],
#     9:  [ 0,  0, "2:6", "4%"],
#     10: [ 0,  0, "2:6", "4%"],
#     11: [ 0,  0, "2:6", "4%"],
#     12: [ 0,  0, "2:6", "4%"],
#     13: [ 1,  0, "3:6", "8%"],
#     14: [ 1,  0, "3:6", "8%"],
#     15: [ 1,  1, "3:6", "16%"],
#     16: [ 1,  1, "3:6", "16%"],
#     17: [ 2,  1, "4:6", "24%"],
#     18: [ 3,  2, "5:6", "32%"],
# }

# con_adj = {
#     3:  [-1, -2, "45%", "1:6", "0%"],
#     4:  [-1, -1, "55%", "1:6", "1%"],
#     5:  [-1, -1, "55%", "1:6", "1%"],
#     6:  [-1, -1, "55%", "1:6", "1%"],
#     7:  [ 0,  0, "65%", "2:6", "2%"],
#     8:  [ 0,  0, "65%", "2:6", "2%"],
#     9:  [ 0,  0, "75%", "2:6", "4%"],
#     10: [ 0,  0, "75%", "2:6", "4%"],
#     11: [ 0,  0, "75%", "2:6", "4%"],
#     12: [ 0,  0, "75%", "2:6", "4%"],
#     13: [ 1,  0, "80%", "3:6", "8%"],
#     14: [ 1,  0, "80%", "3:6", "8%"],
#     15: [ 1,  1, "85%", "3:6", "16%"],
#     16: [ 1,  1, "85%", "3:6", "16%"],
#     17: [ 2,  1, "90%", "4:6", "24%"],
#     18: [ 3,  2, "95%", "5:6", "32%"],
# }

# int_adj = {
#     3:  ["Illiterate", "N/A", "N/A"],
#     4:  ["Illiterate", "N/A", "N/A"],
#     5:  ["Illiterate", "N/A", "N/A"],
#     6:  ["Illiterate", "N/A", "N/A"],
#     7:  ["+0", "N/A", "N/A"],
#     8:  ["+0", "N/A", "N/A"],
#     9:  ["+0", "--", "50%"],
#     10: ["+0", "--", "50%"],
#     11: ["+0", "--", "50%"],
#     12: ["+0", "--", "50%"],
#     13: ["+1", "1st", "65%"],
#     14: ["+1", "1st", "65%"],
#     15: ["+1", "1st, 2nd", "75%"],
#     16: ["+1", "1st, 2nd", "75%"],
#     17: ["+2", "1st, 2nd, 3rd", "85%"],
#     18: ["+3", "1st, 2nd, 3rd, 4th", "95%"],
# }

# wis_adj = {
#     3:  [-2, "N/A", "N/A"],
#     4:  [-1, "N/A", "N/A"],
#     5:  [-1, "N/A", "N/A"],
#     6:  [-1, "N/A", "N/A"],
#     7:  [0, "N/A", "N/A"],
#     8:  [0, "N/A", "N/A"],
#     9:  [0, "--", "50%"],
#     10: [0, "--", "50%"],
#     11: [0, "--", "50%"],
#     12: [0, "--", "50%"],
#     13: [0, "1st", "65%"],
#     14: [0, "1st", "65%"],
#     15: [1, "1st, 2nd", "75%"],
#     16: [1, "1st, 2nd", "75%"],
#     17: [1, "1st, 2nd, 3rd", "85%"],
#     18: [2, "1st, 2nd, 3rd, 4th", "95%"],
# }

# cha_adj = {
#     3:  [-3,  1, -1],
#     4:  [-2,  2, -1],
#     5:  [-2,  2, -1],
#     6:  [-2,  2, -1],
#     7:  [-1,  3,  0],
#     8:  [-1,  3,  0],
#     9:  [ 0,  4,  0],
#     10: [ 0,  4,  0],
#     11: [ 0,  4,  0],
#     12: [ 0,  4,  0],
#     13: [ 1,  6,  0],
#     14: [ 1,  6,  0],
#     15: [ 1,  8,  1],
#     16: [ 1,  8,  1],
#     17: [ 2, 10,  1],
#     18: [ 3, 12,  1],
# }

