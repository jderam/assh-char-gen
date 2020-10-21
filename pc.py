import dice
import random


class PlayerCharacter:

    def _gen_abilities(self):
        abilities = {
            'STR': dice.roll_ndn_drop_n(4,6,1),
            'DEX': dice.roll_ndn_drop_n(4,6,1),
            'CON': dice.roll_ndn_drop_n(4,6,1),
            'INT': dice.roll_ndn_drop_n(4,6,1),
            'WIS': dice.roll_ndn_drop_n(4,6,1),
            'CHA': dice.roll_ndn_drop_n(4,6,1),
        }
        return abilities

    def _get_best_stat(self, abilities: dict) -> str:
        """
        docstring
        """
        top_score = 0
        top_stats = []
        for k, v in abilities.items():
            if v == top_score:
                top_stats.append(k)
            elif v > top_score:
                top_score = v
                top_stats = [k]
            else:
                continue
        if len(top_stats) > 1:
            # give preference to something other than CHA/CON if possible
            top_stats.sort()
            return top_stats[-1]
        else:
            return top_stats[0]

    def _determine_class(self, best_stat):
        stat_map = {
            'STR': 'Fighter',
            'DEX': 'Thief',
            'INT': 'Magician',
            'WIS': 'Cleric',
        }
        if best_stat in stat_map.keys():
            return stat_map[best_stat]
        else:
            return random.choice(list(stat_map.values()))


    def __init__(self):
        self.abilities = self._gen_abilities()
        self.best_stat = self._get_best_stat(self.abilities)
        self.char_class = self._determine_class(self.best_stat)


    


if __name__ == '__main__':
    my_pc = PlayerCharacter()
    print(my_pc.abilities)
    print(f"Best Stat: {my_pc.best_stat}")
    print(f"Class: {my_pc.char_class}")
    # print(my_pc.abilities.index(max(my_pc.abilities.values())))
