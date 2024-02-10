from __future__ import annotations

import numpy as np


class Actor:
    def __init__(self, position: np.array, hitbox_size: int):
        self.position: np.array = position
        self.hitbox_size: int = hitbox_size

    def get_position(self):
        return self.position

    def get_hitbox_size(self):
        return self.hitbox_size
