"""
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from unittest.mock import MagicMock

import numpy as np
import pytest

from py_ability_proto.abilities.base_ability import BaseAbility
from py_ability_proto.actors.base_actor import Actor


def test_constuctor_default(default_actor, reliable_uuid):
    """
    Testing default constructor of BaseAbility and attributes
    """
    ability = BaseAbility(
        owner=default_actor,
        targeted=True,
        precalculate=False,
        direction=np.array([1.0, 1.0, 1.0]),
        speed=2.0,
        damage=2.0,
        hitbox_size=5.0,
    )

    # test uuid
    assert ability.uuid is None
    ability.set_uuid(reliable_uuid)
    assert ability.uuid == reliable_uuid

    # test params
    assert ability.targeted is True
    assert ability.precalculate is False
    assert ability.hitbox_size == 5.0
    assert ability.damage == 2.0
    assert ability.speed == 2.0
    assert all(ability.position == default_actor.get_position())


def test_constructor_faulty_owner():
    """
    Testing default constructor of BaseAbility provoking
    assertion error by providing non-Actor owner.
    """
    mock_owner = MagicMock(spec=['a'])
    with pytest.raises(AssertionError) as excinfo:
        BaseAbility(owner=mock_owner)
    assert 'Owning object does not provide functionality: "get_position"' \
        == str(excinfo.value)


def test_get_classname(default_actor):
    """
    Testing BaseAbility.get_classname
    """
    ability = BaseAbility(owner=default_actor)
    assert ability.get_classname() == 'BaseAbility'


def test_representation(basic_ability, reliable_uuid):
    """
    Testing BaseAbility.__repr__
    """
    basic_ability.set_uuid(reliable_uuid)

    assert str(
        basic_ability,
    ) == f'{basic_ability.get_classname()} with UUID: {reliable_uuid}'


def test_destroy_with_reason(capsys, basic_ability):
    """
    Testing BaseAbility.destroy with reason
    """
    basic_ability.destroy('test')
    capture = capsys.readouterr()
    assert capture.out == 'Destroying ability instance ( test )\n'


def test_tick(basic_ability):
    """
    Testing BaseAbility.tick
    """
    # set position, direction and speed manually
    basic_ability.position = np.asarray([0, 0, 0])
    basic_ability.direction = np.asarray([1, 1, 0])
    basic_ability.speed = 3
    basic_ability.tick()
    assert all(basic_ability.position == np.asarray([3, 3, 0]))


def test_hit(basic_ability):
    """
    Testing BaseAbility.hit
    """
    # hit owner of basic ability
    assert basic_ability.hit(basic_ability.owner) is False

    # hit other actor
    other_actor = Actor([2, 2, 2], 0.1)

    assert not basic_ability.hit(other_actor)
    basic_ability.tick()
    assert basic_ability.hit(other_actor)
