from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_bpla_video_layer, open_main_page, open_map_page, open_start_page, sign_in, show_bpla_video_info, open_bpla_video_object_card, bpla_video_playback


@allure.epic('IS-ECP-GIS')
@allure.title('Видео с БПЛА')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_bpla_video(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    open_bpla_video_layer(app)

    show_bpla_video_info(app, 1378, 321)

    open_bpla_video_object_card(app)

    bpla_video_playback(app)
