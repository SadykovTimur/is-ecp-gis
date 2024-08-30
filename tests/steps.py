from time import sleep
from typing import List

import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page import MainPage
from dit.qa.pages.map_page import MapPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'open_main_page',
    'sign_in',
    'open_map_page',
    'zoom_in_map',
    'zoom_out_map_to_initial_position',
    'measure_distance',
    'select_ortophoto'
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)
            auth_form.login_title.click()

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def open_map_page(app: Application) -> None:
    with allure.step('Opening Map page'):
        try:
            page = MainPage(app)
            page.menu.info.click()
            page.menu.map.click()
            app.driver.switch_to.window(app.driver.window_handles[-1])

            MapPage(app).wait_for_loading()

            screenshot_attach(app, 'map_page')
        except Exception as e:
            screenshot_attach(app, 'map_page_error')

            raise e


def zoom_in_map(app: Application) -> None:
    with allure.step('Zooming in Map'):
        try:
            page = MapPage(app)
            page.zoom_in_map()

            screenshot_attach(app, 'zoom_in_page')
        except Exception as e:
            screenshot_attach(app, 'zoom_in_page_error')

            raise e

        page.zoom_out_map()


def zoom_out_map_to_initial_position(app: Application) -> None:
    with allure.step('Zooming out Map to initial position'):
        try:
            page = MapPage(app)
            page.zoom_in_map()

            page.zoom_out_map_to_initial_position()

            screenshot_attach(app, 'zoom_out_page')
        except Exception as e:
            screenshot_attach(app, 'zoom_out_page_error')

            raise e


def measure_distance(app: Application) -> None:
    with allure.step('Measuring a distance'):
        try:
            page = MapPage(app)
            page.top_buttons.measure.click()
            page.top_buttons.measure_distance.click()

            page.put_a_point_on_map(100, 200)
            page.put_a_point_on_map(150, 350)

            page.check_measure_total()

            screenshot_attach(app, 'distance')
        except Exception as e:
            screenshot_attach(app, 'distance_error')

            raise e


def select_ortophoto(app: Application) -> None:
    with allure.step('Selecting ortophoto'):
        try:
            page = MapPage(app)
            page.sidebar.interface.click()
            page.sidebar.orthophoto.click()

            """
            Как-то тут проверить, что подложка изменилась
            
            """

            sleep(10)

            screenshot_attach(app, 'ortophoto')
        except Exception as e:
            screenshot_attach(app, 'ortophoto_error')

            raise e
