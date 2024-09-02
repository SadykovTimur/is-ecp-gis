from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    open_main_page,
    open_map_page,
    open_start_page,
    sign_in,
    select_control_orders_layer
)


@allure.epic('EKIS-MAYAK')
@allure.title('Поручения мэра')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_mayors_instructions(request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_map_page(app)

    select_control_orders_layer(app, '13.5')
