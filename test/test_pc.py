import pc
import pytest


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_gen_abilities(dummy_parameter):
    player_char = pc.PlayerCharacter()
    print(player_char.abilities)
    assert list(player_char.abilities.keys()) == ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    for v in player_char.abilities.values():
        assert 3 <= v <= 18


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_best_stat(dummy_parameter):
    player_char = pc.PlayerCharacter()
    print(player_char.abilities)
    print(f"calculated best stat: {player_char.best_stat}")
    best_score = max(player_char.abilities.values())
    assert player_char.abilities[player_char.best_stat] == best_score


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_char_class(dummy_parameter):
    player_char = pc.PlayerCharacter()
    assert player_char.char_class in ['Fighter', 'Thief', 'Magician', 'Cleric']
    if player_char.best_stat == 'STR':
        assert player_char.char_class == 'Fighter'
    if player_char.best_stat == 'DEX':
        assert player_char.char_class == 'Thief'
    if player_char.best_stat == 'INT':
        assert player_char.char_class == 'Magician'
    if player_char.best_stat == 'WIS':
        assert player_char.char_class == 'Cleric'


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_spell_list(dummy_parameter):
    player_char = pc.PlayerCharacter()
    if player_char.char_class in ['Cleric', 'Magician']:
        assert len(set(player_char.spell_list)) == 3
    else:
        assert len(player_char.spell_list) == 0


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_class_selection(dummy_parameter):
    player_char = pc.PlayerCharacter()
    if player_char.char_class == 'Fighter':
        assert player_char.abilities['STR'] >= player_char.abilities['DEX']
        assert player_char.abilities['STR'] >= player_char.abilities['INT']
        assert player_char.abilities['STR'] >= player_char.abilities['WIS']
    if player_char.char_class == 'Thief':
        assert player_char.abilities['DEX'] >= player_char.abilities['STR']
        assert player_char.abilities['DEX'] >= player_char.abilities['INT']
        assert player_char.abilities['DEX'] >= player_char.abilities['WIS']
    if player_char.char_class == 'Magician':
        assert player_char.abilities['INT'] >= player_char.abilities['DEX']
        assert player_char.abilities['INT'] >= player_char.abilities['STR']
        assert player_char.abilities['INT'] >= player_char.abilities['WIS']
    if player_char.char_class == 'Cleric':
        assert player_char.abilities['WIS'] >= player_char.abilities['DEX']
        assert player_char.abilities['WIS'] >= player_char.abilities['INT']
        assert player_char.abilities['WIS'] >= player_char.abilities['STR']


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_thief_skills(dummy_parameter):
    player_char = pc.PlayerCharacter()
    if player_char.char_class == 'Thief':
        if player_char.abilities['DEX'] >= 16:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Climb'] == 9
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Hide'] == 6
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Manipulate Traps'] == 4
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Move Silently'] == 6
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Open Locks'] == 4
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Pick Pockets'] == 5
        else:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Climb'] == 8
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Hide'] == 5
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Manipulate Traps'] == 3
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Move Silently'] == 5
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Open Locks'] == 3
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Pick Pockets'] == 4
        
        if player_char.abilities['INT'] >= 16:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Decipher Script'] == 1
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Read Scrolls'] == '-'
        else:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Decipher Script'] == 0
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Read Scrolls'] == '-'

        if player_char.abilities['WIS'] >= 16:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Discern Noise'] == 5
        else:
            assert player_char.char_info['Class Abilities']['Thief Abilities']['Discern Noise'] == 4


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_alignment(dummy_parameter):
    player_char = pc.PlayerCharacter()
    alignments = [
            'Neutral',
            'Lawful Good',
            'Chaotic Good',
            'Lawful Evil',
            'Chaotic Evil',
        ]
    assert player_char.alignment in alignments
    if player_char.char_class == 'Thief':
        assert player_char.alignment != 'Lawful Good'


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_fighting_ability(dummy_parameter):
    player_char = pc.PlayerCharacter()
    assert player_char.fa in [0, 1]
    assert player_char.fighting_ability in ['+0', '+1']


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_ability_adj(dummy_parameter):
    player_char = pc.PlayerCharacter()

    assert player_char.ability_mods['STR'][0] in ['-2', '-1', '+0', '+1', '+2']
    assert player_char.ability_mods['STR'][1] in ['-2', '-1', '+0', '+1', '+2', '+3']
    assert player_char.ability_mods['STR'][2] in [f"{x}:6" for x in range(1, 7)]
    assert player_char.ability_mods['STR'][3] in [f"{x}%" for x in [0,1,2,4,8,16,24,32]]

    assert player_char.ability_mods['DEX'][0] in ['-2', '-1', '+0', '+1', '+2', '+3']
    assert player_char.ability_mods['DEX'][1] in ['-2', '-1', '+0', '+1', '+2']
    assert player_char.ability_mods['DEX'][2] in [f"{x}:6" for x in range(1, 7)]
    assert player_char.ability_mods['DEX'][3] in [f"{x}%" for x in [0,1,2,4,8,16,24,32]]

    assert player_char.ability_mods['CON'][0] in ['-1', '+0', '+1', '+2', '+3']
    assert player_char.ability_mods['CON'][1] in ['-2', '-1', '+0', '+1', '+2']
    assert player_char.ability_mods['CON'][2] in ['45%','55%','65%','75%','80%','85%','90%','95%']
    assert player_char.ability_mods['CON'][3] in [f"{x}:6" for x in range(1, 7)]
    assert player_char.ability_mods['CON'][4] in [f"{x}%" for x in [0,1,2,4,8,16,24,32]]

    assert player_char.ability_mods['INT'][0] in ['Illiterate','+0','+1','+2','+3']
    assert player_char.ability_mods['INT'][1] in ['N/A', '--', '1st', '1st, 2nd' ,'1st, 2nd, 3rd', '1st, 2nd, 3rd, 4th']
    assert player_char.ability_mods['INT'][2] in ['N/A', '50%', '65%', '75%', '85%', '95%']

    assert player_char.ability_mods['WIS'][0] in ['-2', '-1', '+0', '+1', '+2']
    assert player_char.ability_mods['WIS'][1] in ['N/A', '--', '1st', '1st, 2nd' ,'1st, 2nd, 3rd', '1st, 2nd, 3rd, 4th']
    assert player_char.ability_mods['WIS'][2] in ['N/A', '50%', '65%', '75%', '85%', '95%']

    assert player_char.ability_mods['CHA'][0] in ['-3', '-2', '-1', '+0', '+1', '+2', '+3']
    assert player_char.ability_mods['CHA'][1] in [1, 2, 3, 4, 6, 8, 10, 12]
    assert player_char.ability_mods['CHA'][2] in ['-1', '+0', '+1']


@pytest.mark.parametrize("dummy_parameter", range(1000))
def test_save_mods(dummy_parameter):
    player_char = pc.PlayerCharacter()
    for k, v in player_char.save_mods.items():
        assert v in ['+0', '+2']
