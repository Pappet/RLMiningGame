from __future__ import annotations

import lzma
import pickle

from typing import TYPE_CHECKING

from tcod.console import Console
from tcod.map import compute_fov

import project_files.exceptions as exceptions
from project_files.render_functions import render_bar, render_names_at_mouse_location
from project_files.message_log import MessageLog

if TYPE_CHECKING:
    from project_files.game_map import GameMap
    from project_files.entity import Actor


class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.player = player
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)
        self.message_log.render(console=console, x=21,
                                y=45, width=60, height=5)

        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        render_names_at_mouse_location(
            console=console, x=21, y=44, engine=self)

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)
