from time import sleep
from typing import List

import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.bpla_object_card_page import BplaObjectCardPage
from dit.qa.pages.instructions_object_card_page import InstructionsObjectCardPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.map_page import MapPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'open_main_page',
    'sign_in',
    'open_map_page',
    'zoom_by_cursor',
    'zoom_in_map',
    'zoom_out_map_to_initial_position',
    'measure_distance',
    'measure_square',
    'measure_perimetr',
    'select_ortophoto',
    'select_control_orders_layer',
    'show_control_orders_info',
    'open_panoramas_layer',
    'open_panoramas_window',
    'open_cameras_layer',
    'open_bpla_video_layer',
    'open_bpla_panoramas_layer',
    'check_control_orders_info_options',
    'position_map_on_object',
    'open_object_card',
    'show_video_broadcast_and_info',
    'close_video_broadcast',
    'show_bpla_video_info',
    'open_bpla_video_object_card',
    'bpla_video_playback',
    'show_bpla_panoramas_info',
    'open_bpla_panoramas_object_card'
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


def zoom_in_map(app: Application, zoom_value: str) -> None:
    with allure.step('Zooming in Map'):
        try:
            page = MapPage(app)
            page.zoom_in_map(zoom_value)

            screenshot_attach(app, 'zoom_in_map')
        except Exception as e:
            screenshot_attach(app, 'zoom_in_map_error')

            raise e

        page.zoom_out_map('9.4')


def zoom_by_cursor(app: Application) -> None:
    with allure.step('Zooming in Map'):
        try:
            app.driver.execute_script("document.body.style.zoom = '1.5'")
            sleep(5)

            screenshot_attach(app, 'zoom_in_map')
        except Exception as e:
            screenshot_attach(app, 'zoom_in_map_error')

            raise e


def zoom_out_map_to_initial_position(app: Application) -> None:
    with allure.step('Zooming out Map to initial position'):
        try:
            page = MapPage(app)
            page.zoom_in_map('18.4')

            page.zoom_out_map_to_initial_position()

            screenshot_attach(app, 'zoom_out_map')
        except Exception as e:
            screenshot_attach(app, 'zoom_out_map_error')

            raise e


def measure_distance(app: Application, coordinates: list) -> None:
    with allure.step('Measuring a distance'):
        try:
            page = MapPage(app)
            page.top_buttons.measure.click()
            page.top_buttons.measure_distance.click()

            page.put_a_point_on_map(coordinates)

            page.check_measure_total()

            screenshot_attach(app, 'distance')
        except Exception as e:
            screenshot_attach(app, 'distance_error')

            raise e

        page.top_buttons.measure.click()


def measure_square(app: Application, coordinates: list) -> None:
    with allure.step('Measuring a square'):
        try:
            page = MapPage(app)
            page.top_buttons.measure.click()
            page.top_buttons.measure_square.click()

            page.put_a_point_on_map(coordinates)

            page.check_measure_total()

            screenshot_attach(app, 'square')
        except Exception as e:
            screenshot_attach(app, 'square_error')

            raise e

        page.top_buttons.measure.click()


def measure_perimetr(app: Application, coordinates: list) -> None:
    with allure.step('Measuring a perimetr'):
        try:
            page = MapPage(app)
            page.top_buttons.measure.click()
            page.top_buttons.measure_perimeter.click()

            page.put_a_point_on_map(coordinates)

            page.check_measure_total()

            screenshot_attach(app, 'perimetr')
        except Exception as e:
            screenshot_attach(app, 'perimetr_error')

            raise e

        page.top_buttons.measure.click()


def select_ortophoto(app: Application) -> None:
    with allure.step('Selecting ortophoto'):
        try:
            page = MapPage(app)
            page.sidebar.interface.click()
            page.sidebar.orthophoto.click()

            """
            Как-то тут проверить, что подложка изменилась
            
            """

            screenshot_attach(app, 'ortophoto')
        except Exception as e:
            screenshot_attach(app, 'ortophoto_error')

            raise e


def select_control_orders_layer(app: Application, zoom_value: str) -> None:
    with allure.step('Selecting control orders layer'):
        try:
            page = MapPage(app)
            page.sidebar.layers.mayors_instructions.click()
            page.sidebar.layers.control_orders.click()
            page.zoom_in_map(zoom_value)

            screenshot_attach(app, 'control_orders_layer')
        except Exception as e:
            screenshot_attach(app, 'control_orders_layer_error')

            raise e


def show_control_orders_info(app: Application, x_coord: int, y_coord: int) -> None:
    with allure.step('Showing control orders info'):
        try:
            page = MapPage(app)
            page.activate_object_on_map(x_coord, y_coord)

            page.wait_for_loading_info_panel(70, 'Информация о контрольных поручениях не загружена')

            screenshot_attach(app, 'control_orders_info')
        except Exception as e:
            screenshot_attach(app, 'control_orders_info_error')

            raise e


def check_control_orders_info_options(app: Application) -> None:
    with allure.step('Checking control orders info options'):
        try:
            page = MapPage(app)
            page.info_panel.menu.click()

            page.wait_for_loading_control_orders_info_panel_options()

            screenshot_attach(app, 'control_orders_info_options')
        except Exception as e:
            screenshot_attach(app, 'control_orders_info_options_error')

            raise e


def position_map_on_object(app: Application) -> None:
    with allure.step('Positioning map on object'):
        try:
            page = MapPage(app)
            page.info_panel.to_object.click()

            page.wait_for_positioning_map_on_object()

            screenshot_attach(app, 'position_map_on_object')
        except Exception as e:
            screenshot_attach(app, 'position_map_on_object_error')

            raise e


def open_object_card(app: Application) -> None:
    with allure.step('Opening object card'):
        try:
            page = MapPage(app)
            page.info_panel.object_card.click()

            app.driver.switch_to.window(app.driver.window_handles[-1])

            InstructionsObjectCardPage(app).wait_for_loading()

            screenshot_attach(app, 'object_card')
        except Exception as e:
            screenshot_attach(app, 'object_card_error')

            raise e


def open_panoramas_layer(app: Application) -> None:
    with allure.step('Opening panoramas layer'):
        try:
            page = MapPage(app)
            page.top_buttons.panoramas.click()

            page.wait_for_loading_map_layer()

            screenshot_attach(app, 'panoramas_layer')
        except Exception as e:
            screenshot_attach(app, 'panoramas_layer_error')

            raise e


def open_panoramas_window(app: Application, x: int, y: int) -> None:
    with allure.step('Opening panoramas window'):
        try:
            page = MapPage(app)
            page.activate_object_on_map(x, y)

            page.wait_for_loading_panoramas_window()

            screenshot_attach(app, 'panoramas_window')
        except Exception as e:
            screenshot_attach(app, 'panoramas_window_error')

            raise e


def open_cameras_layer(app: Application, zoom_value: str) -> None:
    with allure.step('Opening cameras layer'):
        try:
            page = MapPage(app)
            page.sidebar.search.send_keys('Город Москва, Красная площадь, дом 1')
            page.sidebar.address[-1].click()

            page.sidebar.layers.video_cameras.click()
            page.sidebar.layers.contract_cameras.click()
            page.sidebar.layers.public_places.click()
            page.sidebar.layers.broadcast_is_on.click()
            page.zoom_in_map(zoom_value)

            screenshot_attach(app, 'cameras_layer')
        except Exception as e:
            screenshot_attach(app, 'cameras_layer_error')

            raise e


def show_video_broadcast_and_info(app: Application, x_coord, y_coord) -> None:
    with allure.step('Showing video broadcast and info'):
        try:
            page = MapPage(app)
            page.activate_object_on_map(x_coord, y_coord)

            page.wait_for_loading_video_broadcast_and_info()

            screenshot_attach(app, 'video_broadcast_and_info')
        except Exception as e:
            screenshot_attach(app, 'video_broadcast_and_info_error')

            raise e


def close_video_broadcast(app: Application) -> None:
    with allure.step('Closing video broadcast'):
        try:
            page = MapPage(app)
            page.video_broadcast.close.click()

            page.wait_for_closing_video_broadcast()

            screenshot_attach(app, 'video_broadcast')
        except Exception as e:
            screenshot_attach(app, 'video_broadcast_error')

            raise e


def open_bpla_video_layer(app: Application) -> None:
    with allure.step('Opening BPLA video layer'):
        try:
            page = MapPage(app)
            page.sidebar.layers.aerial_photography.click()
            page.sidebar.layers.bpla_video.click()

            page.wait_for_loading_map_layer()

            screenshot_attach(app, 'bpla_video_layer')
        except Exception as e:
            screenshot_attach(app, 'bpla_video_layer_error')

            raise e


def show_bpla_video_info(app: Application, x_coord: int, y_coord: int) -> None:
    with allure.step('Showing bpla video info'):
        try:
            page = MapPage(app)
            page.activate_object_on_map(x_coord, y_coord)

            page.wait_for_loading_info_panel(160, 'Информация о "Видео с БПЛА" не загружена')

            screenshot_attach(app, 'bpla_video_info')
        except Exception as e:
            screenshot_attach(app, 'bpla_video_info_error')

            raise e


def open_bpla_video_object_card(app: Application) -> None:
    with allure.step('Opening Bpla video object card'):
        try:
            page = MapPage(app)
            page.info_panel.object_card.click()

            app.driver.switch_to.window(app.driver.window_handles[-1])

            BplaObjectCardPage(app).wait_for_loading_bpla_video()

            screenshot_attach(app, 'bpla_video_object_card')
        except Exception as e:
            screenshot_attach(app, 'bpla_video_object_card_error')

            raise e


def bpla_video_playback(app: Application) -> None:
    with allure.step('Playing Bpla video'):
        sleep(3)
        try:
            page = BplaObjectCardPage(app)
            start_time = page.time.split(' / ')[0]
            page.play.click()
            sleep(5)
            page.video_player.click()
            end_time = page.time.split(' / ')[0]

            page.video_playback(start_time, end_time)

            screenshot_attach(app, 'bpla_video')
        except Exception as e:
            screenshot_attach(app, 'bpla_video_error')

            raise e


def open_bpla_panoramas_layer(app: Application) -> None:
    with allure.step('Opening BPLA panoramas layer'):
        try:
            page = MapPage(app)
            page.sidebar.layers.aerial_photography.click()
            page.sidebar.layers.bpla_panoramas.click()

            page.wait_for_loading_map_layer()

            screenshot_attach(app, 'bpla_panoramas_layer')
        except Exception as e:
            screenshot_attach(app, 'bpla_panoramas_layer_error')

            raise e


def show_bpla_panoramas_info(app: Application, x_coord: int, y_coord: int) -> None:
    with allure.step('Showing bpla panoramas info'):
        try:
            page = MapPage(app)
            page.activate_object_on_map(x_coord, y_coord)

            page.wait_for_loading_info_panel(160, 'Информация о "Панорамы 360 с БПЛА" не загружена')

            screenshot_attach(app, 'bpla_panoramas_info')
        except Exception as e:
            screenshot_attach(app, 'bpla_panoramas_info_error')

            raise e


def open_bpla_panoramas_object_card(app: Application) -> None:
    with allure.step('Opening Bpla panoramas object card'):
        try:
            page = MapPage(app)
            page.info_panel.object_card.click()

            app.driver.switch_to.window(app.driver.window_handles[-1])

            BplaObjectCardPage(app).wait_for_loading_bpla_panoramas()

            screenshot_attach(app, 'bpla_panoramas_object_card')
        except Exception as e:
            screenshot_attach(app, 'bpla_panoramas_object_card_error')

            raise e


def select_next_frame(app: Application) -> None:
    with allure.step('Selecting next frame'):
        try:
            pass

            screenshot_attach(app, 'next_frame')
        except Exception as e:
            screenshot_attach(app, 'next_frame_error')

            raise e
