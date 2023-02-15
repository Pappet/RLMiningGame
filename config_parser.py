import configparser as c
import settings
config = c.RawConfigParser()


def Read():
    config = c.RawConfigParser()
    config.read("settings.cfg")

    settings.screen_width = config.getint("ScreenInfo", "screen_width")
    settings.screen_height = config.getint("ScreenInfo", "screen_height")
    settings.title = config.get("ScreenInfo", "title")
    settings.vsync = config.getboolean("ScreenInfo", "vsync")

    settings.map_width = config.getint("MapInfo", "map_width")
    settings.map_height = config.getint("MapInfo", "map_height")
    settings.room_max_size = config.getint("MapInfo", "room_max_size")
    settings.room_min_size = config.getint("MapInfo", "room_min_size")
    settings.max_rooms = config.getint("MapInfo", "max_rooms")
    settings.max_monsters_per_room = config.getint(
        "MapInfo", "max_monsters_per_room")
    settings.max_items_per_room = config.getint(
        "MapInfo", "max_items_per_room")

    settings.font_file = config.get("FontInfo", "font_file")


def Write():
    config.add_section("ScreenInfo")
    config.set("ScreenInfo", "screen_width", "settings.screen_width")
    config.set("ScreenInfo", "screen_height", "settings.screen_height")
    config.set("ScreenInfo", "title", "settings.title")
    config.set("ScreenInfo", "vsync", "settings.vsync")

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

    config.add_section("FontInfo")
    config.set("FontInfo", "font_file", "settings.font_file")
