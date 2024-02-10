from __future__ import annotations

import numpy as np


class BaseAbility():
    def __init__(
            self,
            owner: object = None,
            targeted: bool = False,
            precalculate: bool = True,
            direction: np.array = np.array([0, 0, 0]),
            speed: float = 1,
            damage: float = 1,
            hitbox_size: float = 1,
    ):
        assert hasattr(
            owner, 'get_position',
        ), 'Owning object does not provide functionality: "get_position"'
        self.owner: object = owner

        self.targeted: bool = targeted
        self.precalculate: bool = precalculate
        self.hitbox_size: float = hitbox_size

        self.damage: float = damage
        self.speed: float = speed

        self.position: np.array = self.get_owner_position(
        ) if self.owner else np.array([0, 0, 0])
        self.direction: np.array = direction / np.linalg.norm(direction)

    @classmethod
    def __del__(cls) -> None:
        print('Deleting ability instance')

    def tick(self) -> None:
        self.position = self.position + (self.direction * self.speed)

    def get_owner_position(self) -> np.array:
        return self.owner.get_position()

    def hit(self, actor: object) -> bool:
        if actor == self.owner:
            return False

        actor_position: np.array = actor.get_position()
        actor_hitbox_size: float = actor.get_hitbox_size()
        hitbox_offset = self.hitbox_size + actor_hitbox_size
        actor_distance = np.linalg.norm(actor_position-self.position)
        print(
            'Distance to target:',
            f'{actor_distance <= hitbox_offset}',
        )
        return actor_distance <= hitbox_offset
