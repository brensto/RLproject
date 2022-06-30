from enum import auto, Enum


"""
This file will determine what order to render entities in. This is useful when
more than one entity is in a tile - the player should always be visible, for
example.
"""

class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
