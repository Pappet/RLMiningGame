import configparser as c
import project_files.settings as settings
config = c.RawConfigParser()


def Read():
    config = c.RawConfigParser()
    config.read("config_files/settings.cfg")

    settings.screen_width = config.getint("ScreenInfo", "screen_width")
    settings.screen_height = config.getint("ScreenInfo", "screen_height")
    settings.title = config.get("ScreenInfo", "title")
    settings.autor = config.get("ScreenInfo", "autor")
    settings.vsync = config.getboolean("ScreenInfo", "vsync")
    settings.menu_width = config.getint("ScreenInfo", "menu_width")

    settings.map_width = config.getint("MapInfo", "map_width")
    settings.map_height = config.getint("MapInfo", "map_height")
    settings.room_max_size = config.getint("MapInfo", "room_max_size")
    settings.room_min_size = config.getint("MapInfo", "room_min_size")
    settings.max_rooms = config.getint("MapInfo", "max_rooms")
    settings.max_monsters_per_room = config.getint(
        "MapInfo", "max_monsters_per_room")
    settings.max_items_per_room = config.getint(
        "MapInfo", "max_items_per_room")

    settings.level_up_factor = config.getint("PlayerInfo", "level_up_factor")

    settings.font_file = config.get("FontInfo", "font_file")
    settings.menu_background_file = config.get(
        "FontInfo", "menu_background_file")


def Write():
    config.add_section("ScreenInfo")
    config.set("ScreenInfo", "screen_width", "settings.screen_width")
    config.set("ScreenInfo", "screen_height", "settings.screen_height")
    config.set("ScreenInfo", "title", "settings.title")
    config.set("ScreenInfo", "autor", "settings.autor")
    config.set("ScreenInfo", "vsync", "settings.vsync")
    config.set("ScreenInfo", "menu_width", "settings.menu_width")

    config.add_section("MapInfo")
    config.set("MapInfo", "map_width", "settings.map_width")
    config.set("MapInfo", "map_height", "settings.map_height")
    config.set("MapInfo", "room_max_size", "settings.room_max_size")
    config.set("MapInfo", "room_min_size", "settings.room_min_size")
    config.set("MapInfo", "max_rooms", "settings.max_rooms")
    config.set("MapInfo", "max_monsters_per_room",
               "settings.max_monsters_per_room")
    config.set("MapInfo", "max_items_per_room",
               "settings.max_items_per_room")

    config.add_section("PlayerInfo")
    config.set("PlayerInfo", "level_up_factor", "settings.level_up_factor")

    config.add_section("FontInfo")
    config.set("FontInfo", "font_file", "settings.font_file")
    config.set("FontInfo", "menu_background_file",
               "settings.menu_background_file")
