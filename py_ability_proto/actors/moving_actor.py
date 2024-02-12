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
from base_actor import Actor
from overrides import override


class MovingActor(Actor):
    """
    Implements an actor which is able to move for the
    ability system.
    """

    def __init__(self, position: np.array, hitbox_size: float, speed: float):
        super().__init__(position, hitbox_size)
        self.speed: float = speed

    def move(self, direction: np.array) -> None:
        """
        Implements the movement of the actor given a position to move to.
        """

        direction /= np.linalg.norm(direction)
        self.position += direction * self.speed

    def get_movement_radius(self) -> float:
        """
        Public function returning the possible movement radius per tick.
        """
        return self.speed

    @override
    def tick(self, **kwargs) -> None:
        """
        Updates the Actor object. If 'direction' is provided,
        the Actor will move towards that direction.
        """
        if kwargs['direction']:
            self.move(kwargs['direction'])
