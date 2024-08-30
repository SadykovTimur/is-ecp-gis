from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException
from coms.qa.frontend.pages.component import Component
from selenium.webdriver import ActionChains

from dit.qa.pages.map_page.components.menu import Menu
from dit.qa.pages.map_page.components.right_buttons import RightButtons
from dit.qa.pages.map_page.components.top_buttons import TopButtons

__all__ = ['MapPage']


class MapPage(Page):
    loader = Component(class_name='loader')
    sidebar = Menu(css='[class*="sidebar "]')
    top_buttons = TopButtons(css='[class*="map-buttons top"]')
    right_buttons = RightButtons(css='[class*="map-buttons right"]')
    map = Component(class_name='mapboxgl-canvas')
    measure_info = Text(class_name='measure-info')

    @property
    def loader_is_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def zoom_in_map(self) -> None:
        try:
            while self.right_buttons.zoom_value != '18.4':
                self.right_buttons.zoom_in.click()
        except NoSuchElementException:
            raise Exception('Увеличение масштаба карты не произошло')

    def zoom_out_map(self) -> None:
        try:
            while self.right_buttons.zoom_value != '9.4':
                self.right_buttons.zoom_out.click()
        except NoSuchElementException:
            raise Exception('Уменьшение масштаба карты не произошло')

    def zoom_out_map_to_initial_position(self) -> None:
        self.right_buttons.initial_position.click()

        try:
            assert self.right_buttons.zoom_value == '9.5'
        except AssertionError:
            raise AssertionError('Уменьшение масштаба карты при помощи кнопки "Первоначальная позиция" не произошло')

    def put_a_point_on_map(self, x: int, y: int) -> None:
        ActionChains(self.driver).move_to_element_with_offset(self.map.webelement, x, y).click().perform()

    def check_measure_total(self) -> None:
        try:
            assert self.measure_info.split(' м')[0] != '0'
        except (AssertionError, NoSuchElementException):
            raise Exception('Измерение величины не выполнилось')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.loader_is_hidden
                assert self.sidebar.visible
                assert self.top_buttons.visible
                assert self.map.visible

                return self.right_buttons.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=130, msg='Страница "Карта" не загружена')
        self.app.restore_implicitly_wait()