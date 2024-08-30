from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_main_page, open_start_page, sign_in, open_map_page, zoom_in_map, zoom_out_map_to_initial_position, measure_distance


@allure.epic('EKIS-MAYAK')
@allure.title('Карта 2D')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_map(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    zoom_in_map(app)

    zoom_out_map_to_initial_position(app)

    measure_distance(app)
