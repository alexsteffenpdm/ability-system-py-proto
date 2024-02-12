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
from uuid import uuid4

import numpy as np
import pytest

from py_ability_proto.abilities.base_ability import BaseAbility
from py_ability_proto.actors.base_actor import Actor
from py_ability_proto.entitiyComponentSystem.system import (
    EntityComponentSystem,
)


@pytest.fixture
def default_actor() -> Actor:
    """
    Provides a pytest fixture that instanciates an Actor.
    """
    return Actor(position=np.asarray([1.0, 1.0, 1.0]), hitbox_size=1.0)


@pytest.fixture
def ecs() -> EntityComponentSystem:
    """
    Provides a pytest fixture that instanciates an
    EntitiyComponentSystem (ECS).
    """
    return EntityComponentSystem()


@pytest.fixture
def reliable_uuid() -> str:
    """
    Provides a pytest fixture returning a uuid4.
    """
    return uuid4()


@pytest.fixture
def basic_ability(default_actor) -> BaseAbility:
    # pylint: disable=redefined-outer-name
    """
    Provides a pytest fixture that instanciates a
    BaseAbility.
    """
    return BaseAbility(default_actor)
