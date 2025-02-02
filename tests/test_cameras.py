from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    close_video_broadcast,
    open_cameras_layer,
    open_main_page,
    open_map_page,
    open_start_page,
    show_video_broadcast_and_info,
    sign_in,
)


@allure.epic('IS-ECP-GIS')
@allure.title('Камеры')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_cameras(request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    open_cameras_layer(app, '17.0')

    show_video_broadcast_and_info(app, 1008, 560)

    close_video_broadcast(app)
