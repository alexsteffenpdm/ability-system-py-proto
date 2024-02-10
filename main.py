from __future__ import annotations

import numpy as np

from src.abilities.base import BaseAbility
from src.dummy_actor import Actor


if __name__ == '__main__':
    emitter = Actor(position=np.array([0, 0, 0]), hitbox_size=1)
    target = Actor(position=np.array([10, 10, 0]), hitbox_size=0.2)

    ability = BaseAbility(
        owner=emitter,
        targeted=False,
        precalculate=False,
        direction=np.array([1, 1, 0]),
        speed=1.4142,
        damage=1.0,
        hitbox_size=0.2,
    )

    # travel length should be 14.142
    print(
        'Expecting to hit up from:'
        f'{(ability.hitbox_size + target.hitbox_size)}',
    )
    while (not ability.hit(target)):
        ability.tick()
        # print(f"Ability position: {ability.position}")

    print('Ability hit target')
    print(
        f'Ability position: {ability.position}\n',
        f'Target_position:{target.get_position()}\n',
    )
    del ability
