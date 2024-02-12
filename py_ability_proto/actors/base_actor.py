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


class Actor:
    """
     Implements a base class for the ability system.
     All actors will be derived from here.
     """

    def __init__(self, position: np.array, hitbox_size: float):
        self.position: np.array = position
        self.hitbox_size: float = hitbox_size
        self.uuid: str = None

    @classmethod
    def __del__(cls) -> None:
        """
        Class destructor.
        """

    @classmethod
    def get_classname(cls):
        """
        Getter for classname string.
        """
        return cls.__name__

    def __repr__(self) -> str:
        return f'{self.get_classname()} with UUID: {self.uuid}'

    def tick(self, **kwargs) -> None:
        """
        Updates the Actor object.
        """
        raise NotImplementedError

    def get_position(self) -> np.array:
        """
        Public function returning the position of the object
        """
        return self.position

    def get_hitbox_size(self) -> float:
        """
        Public function returning the radius of the hitbox of the object
        """
        return self.hitbox_size

    def set_uuid(self, uid: str | None) -> None:
        """
        Setter for uuid.
        """
        self.uuid = uid
