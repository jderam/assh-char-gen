import dice
import random
from tables.ability_adj import adjustments, adj_descriptions
from tables.class_info import class_info
from tables.spells import assh_magician_spells, assh_cleric_spells, dying_earth_spells


def mod_to_str(mod: int) -> str:
    if mod >= 0:
        mod_str = f"+{mod}"
    else:
        mod_str = f"{mod}"
    return mod_str


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
    

    def _lookup_mods(self, abilities: dict) -> dict:
        ability_mods = {}
        for a in abilities.keys():
            ability_mods[a] = adjustments[a][abilities[a]]
        return ability_mods


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


    def _spell_list(self):
        spell_list = []
        if self.char_class == 'Cleric':
            if self.cleric_spell_src == 'assh_cleric_spells':
                spell_list = random.sample(assh_cleric_spells[1], k=3)
            else:
                pass
        elif self.char_class == 'Magician':
            if self.magician_spell_src == 'assh_magician_spells':
                spell_list = random.sample(assh_magician_spells[1], k=3)
            elif self.magician_spell_src == 'dying_earth':
                spell_list.append(random.choice(dying_earth_spells['Offensive'])['name'])
                spell_list.append(random.choice(dying_earth_spells['Defensive'])['name'])
                spell_list.append(random.choice(dying_earth_spells['Miscellaneous'])['name'])
            else:
                pass
        else:
            pass
        spell_list.sort()
        return spell_list


    def __init__(
                 self,
                 class_choice='random',
                 cleric_spell_src='assh_cleric_spells',
                 magician_spell_src='assh_magician_spells',
                ):
        self.class_choice = class_choice
        self.cleric_spell_src = cleric_spell_src
        self.magician_spell_src = magician_spell_src

        self.abilities = self._gen_abilities()
        self.ability_mods = self._lookup_mods(self.abilities)
        self.best_stat = self._get_best_stat(self.abilities)
        self.char_class = self._determine_class(self.best_stat)
        self.char_info = class_info[self.char_class]
        self.hp = self.char_info['HD'] + self.ability_mods['CON'][0]
        self.fa = self.char_info['FA']
        self.armor = self.char_info['Armor']['Type']
        self.ac = self.char_info['Armor']['AC'] + self.ability_mods['DEX'][1]
        self.dr = self.char_info['Armor']['DR']
        self.mv = self.char_info['Armor']['MV']
        self.base_save = 16
        self.save_mods = self.char_info['Saving Throws']
        self.spell_list = self._spell_list()


    


if __name__ == '__main__':
    my_pc = PlayerCharacter(magician_spell_src='dying_earth')
    print(f"Class: {my_pc.char_class}")
    print(f"Hit Points: {my_pc.hp}")
    print(f"Fighting Ability: {mod_to_str(my_pc.fa)}")
    print()
    print(f"Armor Worn: {my_pc.armor}")
    print(f"AC: {my_pc.ac}   DR: {my_pc.dr}   MV: {my_pc.mv}")
    print()
    for k in my_pc.ability_mods.keys():
        print(f"{k}: {my_pc.abilities[k]}")
        for i in range(len(my_pc.ability_mods[k])):
            print(f"   {adj_descriptions[k]['short'][i]}: {my_pc.ability_mods[k][i]}")
        print()
    print(f"Saving Throw: {my_pc.base_save}")
    for k, v in my_pc.save_mods.items():
        print(f"   {k}: {v}")
    print()
    print(f"Spells: {my_pc.spell_list}")
