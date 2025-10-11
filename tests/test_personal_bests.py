from versecbot_personal_bests.jobs import (
    contains_image,
    contains_video,
    contains_personal_best,
)
import pytest


class MockAttachment:
    def __init__(self, content_type: str):
        self.content_type = content_type


TEST_CONTENT_TYPES = [
    {"content_type": "application", "contains": []},
    {"content_type": "application/json", "contains": []},
    {"content_type": "audio", "contains": []},
    {"content_type": "image/png", "contains": ["image"]},
    {"content_type": "image/jpeg", "contains": ["image"]},
    {"content_type": "message", "contains": []},
    {"content_type": "multipart", "contains": []},
    {"content_type": "text", "contains": []},
    {"content_type": "video", "contains": ["video"]},
    {"content_type": "video/mp4", "contains": ["video"]},
    {"content_type": "video/VP9", "contains": ["video"]},
    {"content_type": "font", "contains": []},
    {"content_type": "example", "contains": []},
    {"content_type": "model", "contains": []},
    {"content_type": "haptics", "contains": []},
]


@pytest.mark.parametrize("test_case", TEST_CONTENT_TYPES)
def test_contains_image(test_case: dict[str, str | list[str]]) -> None:
    attachment = MockAttachment(test_case["content_type"])  # type: ignore
    assert contains_image(attachment) is ("image" in test_case["contains"])


@pytest.mark.parametrize("test_case", TEST_CONTENT_TYPES)
def test_contains_video(test_case: dict[str, str | list[str]]) -> None:
    attachment = MockAttachment(test_case["content_type"])  # type: ignore
    assert contains_video(attachment) is ("video" in test_case["contains"])


@pytest.mark.parametrize("test_case", TEST_CONTENT_TYPES)
def test_contains_personal_best(test_case: dict[str, str | list[str]]) -> None:
    attachments = [MockAttachment(test_case["content_type"])]  # type: ignore
    assert contains_personal_best(attachments) is (len(test_case["contains"]) > 0)
