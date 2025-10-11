from versecbot_personal_bests.settings import PersonalBestsSettings
from tomli import load


def test_parse_config() -> None:
    with open("tests/test_config.toml", "rb") as f:
        parsed = load(f)

    config = PersonalBestsSettings.model_validate(
        parsed["versecbot"]["plugins"]["personal_bests"]
    )

    assert config.enabled is True
    assert len(config.handlers) == 2

    first_handler = config.handlers[0]
    assert first_handler.channel_ids == [1]
    assert first_handler.emoji_id == 1
    assert first_handler.create_thread is True

    second_handler = config.handlers[1]
    assert second_handler.channel_ids == [2]
    assert second_handler.emoji_id == 2
    assert second_handler.create_thread is False
