import dice


class PlayerCharacter:

    def __init__(self):
        self.abilities = {
            'STR': dice.roll_ndn_drop_n(4,6,1),
            'DEX': dice.roll_ndn_drop_n(4,6,1),
            'CON': dice.roll_ndn_drop_n(4,6,1),
            'INT': dice.roll_ndn_drop_n(4,6,1),
            'WIS': dice.roll_ndn_drop_n(4,6,1),
            'CHA': dice.roll_ndn_drop_n(4,6,1),
        }

        def choose_class(self):
            pass

    # def stats(self):
    #     stats_list = [
    #         self.STR,
    #         self.DEX,
    #         self.CON,
    #         self.INT,
    #         self.WIS,
    #         self.CHA,
    #     ]
    #     return stats_list
    
my_pc = PlayerCharacter()

if __name__ == '__main__':
    print(my_pc.abilities)

    # print(my_pc.abilities.index(max(my_pc.abilities.values())))
