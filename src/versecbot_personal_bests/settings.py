from versecbot_interface import PluginSettings, WatcherSettings


class HandlePersonalBestSettings(WatcherSettings):
    enabled: bool
    emoji_id: int
    create_thread: bool


class PersonalBestsSettings(PluginSettings):
    handlers: list[HandlePersonalBestSettings]
