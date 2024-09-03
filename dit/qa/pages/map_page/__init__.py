from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException
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
    panoramas_img = Component(class_name='imap-container')
    panoramas_loader = Component(tag='map-core-spinner')

    @property
    def loader_is_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    @property
    def panoramas_loader_is_hidden(self) -> bool:
        try:
            return not self.panoramas_loader.visible
        except NoSuchElementException:
            return True

    def zoom_in_map(self, zoom: str) -> None:
        try:
            while self.right_buttons.zoom_value != zoom:
                self.right_buttons.zoom_in.click()
        except NoSuchElementException:
            raise Exception('Увеличение масштаба карты не произошло')

    def zoom_out_map(self, zoom: str) -> None:
        try:
            while self.right_buttons.zoom_value != zoom:
                self.right_buttons.zoom_out.click()
        except NoSuchElementException:
            raise Exception('Уменьшение масштаба карты не произошло')

    def zoom_out_map_to_initial_position(self) -> None:
        self.right_buttons.initial_position.click()

        try:
            assert self.right_buttons.zoom_value == '9.5'
        except AssertionError:
            raise AssertionError('Уменьшение масштаба карты при помощи кнопки "Первоначальная позиция" не произошло')

    def put_a_point_on_map(self, coordinates: list) -> None:
        for point in coordinates:
            ActionChains(self.driver).move_to_element_with_offset(self.map.webelement, point['x'], point['y']).click().perform()  # type: ignore[no-untyped-call]

    def activate_point_on_map(self, x: int, y: int) -> None:
        ac = ActionChains(self.driver)
        ac.move_to_element(self.right_buttons.zoom_in.webelement)  # type: ignore[no-untyped-call]
        location = self.right_buttons.zoom_in.webelement.location
        ac.move_by_offset(
            x - location['x'], y - location['y']
        ).click().perform()  # type: ignore[no-untyped-call]

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

    def wait_for_loading_panoramas_layer(self) -> None:
        def condition() -> bool:
            try:
                return self.loader_is_hidden

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=100, msg='Режим "Панорамы" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_panoramas_window(self) -> None:
        def condition() -> bool:
            try:
                # assert self.panoramas_loader_is_hidden

                return self.panoramas_img.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=140, msg='Окно "Панорамы" не загружено')
        self.app.restore_implicitly_wait()

