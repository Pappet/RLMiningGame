#!/usr/bin/env python3
import tcod
import copy
import traceback

import project_files.entity_factories as entity_factories
from project_files.engine import Engine
from project_files.procgen import generate_dungeon
import project_files.color as color
import project_files.settings as settings
import project_files.config_parser as config_parser


def main() -> None:
    load_data()

    tileset = tcod.tileset.load_tilesheet(
        settings.font_file, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=settings.max_rooms,
        room_min_size=settings.room_min_size,
        room_max_size=settings.room_max_size,
        map_width=settings.map_width,
        map_height=settings.map_height,
        max_monsters_per_room=settings.max_monsters_per_room,
        max_items_per_room=settings.max_items_per_room,
        engine=engine
    )

    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )

    with tcod.context.new_terminal(
        settings.screen_width,
        settings.screen_height,
        tileset=tileset,
        title=settings.title,
        vsync=settings.vsync,
    ) as context:
        root_console = tcod.Console(
            settings.screen_width, settings.screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error in stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(
                    traceback.format_exc(), color.error)


def load_data():
    config_parser.Read()


if __name__ == "__main__":
    main()
