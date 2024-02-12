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
import numpy as np


class BaseAbility:
    """
    Implements a base class for the ability system.
    All abilities will be derived from here.
    """

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-arguments

    def __init__(
            self,
            owner: object = None,
            targeted: bool = False,
            precalculate: bool = True,
            direction: np.array = np.array([1.0, 1.0, 1.0]),
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

        self.position: np.array = self.owner.get_position(
        ) if self.owner else np.array([0, 0, 0])
        self.origin: np.array = self.position
        self.direction: np.array = direction / np.linalg.norm(direction)

        self.uuid = None

    @classmethod
    def __del__(cls) -> None:
        """
        Class destructor.
        """
        return

    @classmethod
    def get_classname(cls):
        """
        Getter for classname string.
        """
        return cls.__name__

    def __repr__(self) -> str:
        return f'{self.get_classname()} with UUID: {self.uuid}'

    @classmethod
    def destroy(cls, reason: str) -> None:
        """
        Class destructor, providing destruction reason.
        """
        print(f'Destroying ability instance ( {reason} )')
        del cls

    def tick(self) -> None:
        """
        Updates the position of the ability (simulates projectile).
        """
        self.position = self.position + (self.direction * self.speed)

    def hit(self, actor: object) -> bool:
        """
        Hit registration which checks whether the distance between ability
        projectile and target is smaller than the combined hitboxes.
        """
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

    def set_uuid(self, uid: str | None) -> None:
        """
        Setter for uuid.
        """
        self.uuid = uid
