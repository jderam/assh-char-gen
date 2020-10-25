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


def dot_pad(s: str, chars: int) -> str:
    n = chars - len(s)
    return '.' * n


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
    

    def _lookup_mods(self) -> dict:
        ability_mods = {}
        for a in self.abilities.keys():
            ability_mods[a] = adjustments[a][self.abilities[a]]
        return ability_mods


    def _get_stats_ranked(self):
        """
        docstring
        """
        stats_ranked = sorted(self.abilities, key=self.abilities.get, reverse=True)
        return stats_ranked


    def _determine_class(self):
        stat_map = {
            'STR': 'Fighter',
            'DEX': 'Thief',
            'INT': 'Magician',
            'WIS': 'Cleric',
        }
        for s in self.stats_ranked:
            if s in stat_map.keys():
                return stat_map[s]


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
    

    def _update_thief_abilities(self):
        if self.abilities['DEX'] >= 16:
            self.char_info['Class Abilities']['Thief Abilities']['Climb'] += 1
            self.char_info['Class Abilities']['Thief Abilities']['Hide'] += 1
            self.char_info['Class Abilities']['Thief Abilities']['Manipulate Traps'] += 1
            self.char_info['Class Abilities']['Thief Abilities']['Move Silently'] += 1
            self.char_info['Class Abilities']['Thief Abilities']['Open Locks'] += 1
            self.char_info['Class Abilities']['Thief Abilities']['Pick Pockets'] += 1
        if self.abilities['INT'] >= 16:
            self.char_info['Class Abilities']['Thief Abilities']['Decipher Script'] += 1
            # Cannot read scrolls until level 5
            # self.char_info['Class Abilities']['Thief Abilities']['Read Scrolls'] += 1
        if self.abilities['WIS'] >= 16:
            self.char_info['Class Abilities']['Thief Abilities']['Discern Noise'] += 1
        return


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
        self.ability_mods = self._lookup_mods()
        self.stats_ranked = self._get_stats_ranked()
        self.best_stat = self.stats_ranked[0]
        self.char_class = self._determine_class()
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
        if self.char_class == 'Thief':
            self._update_thief_abilities()


    


if __name__ == '__main__':
    my_pc = PlayerCharacter(magician_spell_src='dying_earth')
    print(f"Class: {my_pc.char_class}")
    print(f"Hit Points: {my_pc.hp}")
    print(f"Fighting Ability: {mod_to_str(my_pc.fa)}")
    print()
    print(f"Armor Worn: {my_pc.armor}")
    print(f"AC: {my_pc.ac}   DR: {my_pc.dr}   MV: {my_pc.mv}")
    print()
    print(f"Abilities: {my_pc.abilities}")
    print(f"Best Stat: {my_pc.best_stat}")
    print(f"Stats Ranked: {my_pc.stats_ranked}")
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
    print()
    print(f"Class Abilities: {list(my_pc.char_info['Class Abilities'])}")
    if my_pc.char_class == 'Thief':
        print(my_pc.char_info['Class Abilities']['Thief Abilities'])
        for k, v in my_pc.char_info['Class Abilities']['Thief Abilities'].items():
            print(f"{k}{dot_pad(k,20)}{v}:12")
