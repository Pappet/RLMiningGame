from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool_),  # True if this tile can be walked over.
        ("transparent", np.bool_),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (0, 0, 100), (50, 50, 150)),
    light=(ord(">"), (255, 255, 255), (200, 180, 50)),
)
stone = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (51, 51, 51)),
    light=(ord(" "), (255, 255, 255), (204, 204, 204)),
)
sand = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("."), (255, 255, 255), (139, 121, 94)),
    light=(ord("."), (255, 255, 255), (245, 222, 179)),
)
ore = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("°"), (255, 255, 255), (135, 102, 51)),
    light=(ord("°"), (255, 255, 255), (205, 175, 149)),
)

Marker_green = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (255, 255, 255), (0, 255, 0)),
    light=(ord("#"), (255, 255, 255), (0, 255, 0)),
)
Marker_red = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (255, 255, 255), (255, 0, 0)),
    light=(ord("#"), (255, 255, 255), (255, 0, 0)),
)
