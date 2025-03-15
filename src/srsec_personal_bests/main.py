from discord import Client, Emoji, Message, TextChannel
import re

from speedrun_secretary.jobs import Watcher

from .settings import HandlerSettings
from .logging import logger


class HandlePersonalBest(Watcher):
    enabled: bool
    emoji: Emoji
    channel: TextChannel
    create_thread: bool

    EMOTE_PATTERN = re.compile(r"<:(\S+):\d+>")

    def __init__(self, client: Client, settings: HandlerSettings):
        super().__init__(settings, logger=logger)
        logger.debug("Getting emoji with id %s", settings.emoji_id)
        self.emoji = client.get_emoji(int(settings.emoji_id))
        self.create_thread = settings.create_thread

    def should_act(self, message: Message) -> bool:
        if not super().should_act(message):
            return False

        if not message.attachments:
            return False

        return any(
            "image" in attachment.content_type or "video" in attachment.content_type
            for attachment in message.attachments
        )

    async def act(self, message: Message):
        logger.info(
            "Handling message %s from %s <%s>",
            message.id,
            message.author.name,
            message.author.id,
        )
        logger.debug("[%s] Adding reaction.", message.id)
        await message.add_reaction(self.emoji)

        if self.create_thread:
            if message.content:
                thread_title = message.content

                # Replace emote strings with names
                thread_title = re.sub(
                    self.EMOTE_PATTERN, lambda e: ":" + e.group(1) + ":", thread_title
                )

                # Trim down to 50 characters
                original_length = len(thread_title)
                thread_title = thread_title[:50]
                if len(thread_title) < original_length:
                    thread_title += "..."

            else:
                thread_title = f"Discuss {message.author}'s PB here!"

            logger.debug(
                "[%s] Creating thread with title %s.", message.id, thread_title
            )
            await message.create_thread(name=thread_title)
