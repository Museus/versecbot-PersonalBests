from logging import getLogger

from discord import Intents
from versecbot_interface import Plugin

from .jobs import HandlePersonalBest
from .settings import PersonalBestsSettings, HandlePersonalBestSettings


logger = getLogger("versecbot.plugins.personal_bests")


class PersonalBestsPlugin(Plugin):
    name: str = "personal_bests"
    intents = [Intents.guild_messages]

    def __init__(self):
        super().__init__()

    def initialize(self, settings: PersonalBestsSettings, client):
        logger.info(
            "Initializing Personal Best Reactions plugin...",
        )

        # Register Personal Best Reactions
        for handler_settings_raw in settings.handlers:
            handler_settings = HandlePersonalBestSettings.model_validate(
                handler_settings_raw
            )

            try:
                pb_handler = HandlePersonalBest(client, handler_settings)
            except Exception:
                logger.exception(
                    "Failed to initialize Personal Bests handler for channels %s",
                    ", ".join(handler_settings.channel_ids),
                )
            else:
                self.assign_job(pb_handler)
                logger.info(
                    "Handling personal bests in #%s with Emoji: %s",
                    pb_handler.channel,
                    pb_handler.emoji,
                )

        logger.debug("Personal Bests initialized")
