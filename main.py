#!/usr/bin/env python3
import tcod
import traceback

import project_files.exceptions as exceptions
import project_files.input_handlers as input_handlers
import project_files.color as color
import project_files.settings as settings
import project_files.config_parser as config_parser
import project_files.setup_game as setup_game


def main() -> None:
    load_data()

    tileset = tcod.tileset.load_tilesheet(
        settings.font_file, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
        settings.screen_width,
        settings.screen_height,
        tileset=tileset,
        title=settings.title,
        vsync=settings.vsync,
    ) as context:
        root_console = tcod.Console(
            settings.screen_width, settings.screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


def load_data():
    config_parser.Read()


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        config_parser.Write()
        handler.engine.save_as(filename)
        print("Game saved.")


if __name__ == "__main__":
    main()
