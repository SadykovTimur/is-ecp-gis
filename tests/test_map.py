from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from dit.qa.pages.coordinates import distance_coordinates, perimetr_coordinates, square_coordinates
from tests.steps import (
    measure_distance,
    measure_perimetr,
    measure_square,
    open_main_page,
    open_map_page,
    open_start_page,
    sign_in,
    zoom_by_cursor,
    zoom_in_map,
    zoom_out_map_to_initial_position,
)


@allure.epic('IS-ECP-GIS')
@allure.title('Карта 2D')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_map(request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    zoom_by_cursor(app)

    zoom_in_map(app, '18.4')

    zoom_out_map_to_initial_position(app)

    measure_distance(app, distance_coordinates)

    measure_square(app, square_coordinates)

    measure_perimetr(app, perimetr_coordinates)
