from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from project_files.engine import Engine
    from project_files.entity import Entity
    from project_files.game_map import GameMap


class BaseComponent:
    parent: Entity  # Owning entity instance.

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine
