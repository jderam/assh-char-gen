import pytest
import dice

def test_dice_roll():
    """
    docstring
    """
    rolls = []
    for i in range(1000):
        rolls.append(dice.roll_ndn(1, 6))
    assert len([x for x in rolls if x < 1]) == 0
    assert len([x for x in rolls if x > 6]) == 0

