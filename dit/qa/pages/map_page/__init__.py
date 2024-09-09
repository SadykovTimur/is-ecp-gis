from decimal import Decimal

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from dit.qa.pages.map_page.components.info_panel import InfoPanel
from dit.qa.pages.map_page.components.menu import Menu
from dit.qa.pages.map_page.components.right_buttons import RightButtons
from dit.qa.pages.map_page.components.top_buttons import TopButtons
from dit.qa.pages.map_page.components.video_broadcast import VideoBroadcast
from selenium.webdriver.common.actions.mouse_button import MouseButton

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
    info_panel = InfoPanel(css='[class*="info-results"]')
    video_broadcast = VideoBroadcast(class_name='camera-container')

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

    def zoom_by_cursor(self, zoom_in: bool = True) -> None:
        try:
            ac = ActionChains(self.driver)

            if zoom_in:
                while not Decimal(self.right_buttons.zoom_value) >= Decimal('18.4'):
                    ac.scroll_by_amount(0, -2100).perform()
                    self.wait_loader_is_hidden()
            else:
                while not Decimal(self.right_buttons.zoom_value) <= Decimal('9.5'):
                    ac.scroll_by_amount(0, 2100).perform()
                    self.wait_loader_is_hidden()

        except NoSuchElementException as e:
            raise NoSuchElementException('Увеличение масштаба карты не произошло') from e

    def zoom_in_map(self, zoom: str) -> None:
        try:
            while self.right_buttons.zoom_value != zoom:
                self.right_buttons.zoom_in.click()
        except NoSuchElementException as e:
            raise NoSuchElementException('Увеличение масштаба карты не произошло') from e

    def zoom_out_map(self, zoom: str) -> None:
        try:
            while self.right_buttons.zoom_value != zoom:
                self.right_buttons.zoom_out.click()
        except NoSuchElementException as e:
            raise NoSuchElementException('Уменьшение масштаба карты не произошло') from e

    def zoom_out_map_to_initial_position(self) -> None:
        self.right_buttons.initial_position.click()

        try:
            assert self.right_buttons.zoom_value == '9.5'
        except AssertionError as e:
            raise AssertionError(
                'Уменьшение масштаба карты при помощи кнопки "Первоначальная позиция" не произошло'
            ) from e

    def change_map_orientation(self) -> None:
        ac = ActionChains(self.driver)  # type: ignore[no-untyped-call]
        ac.move_to_element(self.top_buttons.info.webelement)
        ac.move_by_offset(20, 20).perform()  # type: ignore[no-untyped-call]

        ac.w3c_actions.pointer_action.pointer_down(button=MouseButton.RIGHT)
        ac.w3c_actions.key_action.pause()
        ac.move_by_offset(-100, 50)
        ac.w3c_actions.pointer_action.release(button=MouseButton.RIGHT)
        ac.perform()  # type: ignore[no-untyped-call]

    def put_a_point_on_map(self, coordinates: list) -> None:
        for point in coordinates:
            ac = ActionChains(self.driver)  # type: ignore[no-untyped-call]
            ac.move_to_element_with_offset(
                self.map.webelement, point['x'], point['y']
            ).click().perform()  # type: ignore[no-untyped-call]

    def activate_object_on_map(self, x: int, y: int) -> None:
        ac = ActionChains(self.driver)  # type: ignore[no-untyped-call]
        ac.move_to_element(self.top_buttons.info.webelement)  # type: ignore[no-untyped-call]
        location = self.top_buttons.info.webelement.location
        ac.move_by_offset(x - location['x'], y - location['y']).click().perform()  # type: ignore[no-untyped-call]

    def check_measure_total(self) -> None:
        try:
            assert self.measure_info.split(' м')[0] != '0'
        except AssertionError as e:
            raise AssertionError('Измерение величины не выполнилось') from e

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

    def wait_for_loading_map_layer(self) -> None:
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
                assert self.panoramas_loader_is_hidden

                return self.panoramas_img.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=140, msg='Окно "Панорамы" не загружено')
        self.app.restore_implicitly_wait()

    def wait_for_loading_info_panel(self, timeout: int, msg: str) -> None:
        def condition() -> bool:
            try:
                return self.info_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=timeout, msg=msg)
        self.app.restore_implicitly_wait()

    def wait_for_loading_control_orders_info_panel_options(self) -> None:
        def condition() -> bool:
            try:
                return self.info_panel.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(
            condition,
            timeout=70,
            msg='Элементы: "Позиционировать карту на объекте", '
            '"открыть карточку объекта", "Сформировать CSV файл с координатами" недоступны',
        )
        self.app.restore_implicitly_wait()

    def wait_for_positioning_map_on_object(self) -> None:
        def condition() -> bool:
            try:
                return '18.4' == self.right_buttons.zoom_value

            except AssertionError:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Позиционирование карты на объекте не выполнено')
        self.app.restore_implicitly_wait()

    def wait_for_loading_video_broadcast_and_info(self) -> None:
        def condition() -> bool:
            try:
                assert self.info_panel.visible

                return self.video_broadcast.visible

            except AssertionError:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=160, msg='Видеотрансляция  и информационная панель не загружены')
        self.app.restore_implicitly_wait()

    def wait_for_closing_video_broadcast(self) -> None:
        def condition() -> bool:
            try:
                return not self.video_broadcast.visible

            except NoSuchElementException:

                return True

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=100, msg='Окно видеотрансляции не закрыто')
        self.app.restore_implicitly_wait()

    def wait_loader_is_hidden(self) -> None:
        def condition() -> bool:
            try:
                return self.loader_is_hidden

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Карта не загружена')
        self.app.restore_implicitly_wait()

    def wait_changing_orientation(self) -> None:
        def condition() -> bool:
            try:
                assert self.loader_is_hidden
                assert "rotate" in self.right_buttons.rotate

                return "rotate(0deg)" not in self.right_buttons.rotate

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ориентация карты не изменилась')
        self.app.restore_implicitly_wait()

    def wait_restore_orientation(self) -> None:
        def condition() -> bool:
            try:
                assert self.loader_is_hidden

                return "rotate(0deg)" in self.right_buttons.rotate

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ориентация карты не вернулась в исходное положение')
        self.app.restore_implicitly_wait()
