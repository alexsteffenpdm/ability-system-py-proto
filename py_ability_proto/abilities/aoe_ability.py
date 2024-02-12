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
from base_ability import BaseAbility
from overrides import override

from py_ability_proto.actors.base_actor import Actor


class AOEAbility(BaseAbility):
    """
    Implmements a class for area of effect abilities.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=arguments-renamed

    def __init__(
            self,
            owner: Actor = None,
            target_position: np.array = np.array([0, 0, 0]),
            speed: float = 1,
            damage: float = 1,
            hitbox_size: float = 1,
            maxrange: float = 100,
            ensure_int_stepsize: bool = True,
    ):
        super().__init__(
            owner=owner,
            targeted=True,
            speed=speed,
            damage=damage,
            hitbox_size=hitbox_size,
            direction=self.__calculate_direction_from_target_position(
                target_position, owner,
            ),
        )
        self.range = maxrange
        self.target_position = target_position
        assert np.linalg.norm(target_position-self.origin) <= maxrange, \
            'Target position is out of the abilities range.'

        if ensure_int_stepsize:
            self.__recalculate_speed()

        # Ensure speed and positions parameters fit together,
        # in order to avoid overshooting on hitreg.

        assert np.linalg.norm(self.target_position-self.origin)

    def __recalculate_speed(self) -> None:
        """
        Private function, recalculating the abilities speed,
        such that it will land at target position with a natural
        number of steps.
        """
        travel_length = np.linalg.norm(self.target_position - self.origin)
        steps = round(travel_length / self.speed)

        if not np.isclose(steps, (travel_length / self.speed)):
            # speed * fl_steps == x * int_steps
            self.speed = ((travel_length / self.speed) * self.speed) / steps

    def __calculate_direction_from_target_position(
            self,
            target_position: np.array,
            owner: Actor,
    ) -> np.array:
        """
        Private function, calculating the abilities normalized
        direction based on the provided target position.
        """

        direction: np.array = target_position - owner.get_position()
        return direction / np.linalg.norm(direction)

    @override
    def tick(self) -> None:
        """
        Updates the position of the ability (simulates projectile).
        Triggers descructor if the traveled range is reached
        """

        if np.linalg.norm(self.position-self.origin) >= self.range:
            self.destroy('Range reached')
        else:
            super().tick()

    def hit(self, actors: list[Actor]) -> list[Actor]:
        """
        Calculates the actors hit at destination
        """
        return actors
