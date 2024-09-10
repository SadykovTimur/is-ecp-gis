from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    check_control_orders_info_options,
    open_main_page,
    open_map_page,
    open_object_card,
    open_start_page,
    position_map_on_object,
    select_control_orders_layer,
    show_control_orders_info,
    sign_in,
)


@allure.epic('IS-ECP-GIS')
@allure.title('Поручения мэра')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_mayors_instructions(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    select_control_orders_layer(app, '13.5')

    show_control_orders_info(app, 1781, 363)

    check_control_orders_info_options(app)

    position_map_on_object(app)

    check_control_orders_info_options(app)

    open_object_card(app)
