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

