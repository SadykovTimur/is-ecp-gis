from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException
from coms.qa.frontend.pages.component import Component
from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.main import Main
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(tag='cdp-navbar')
    menu = Menu(tag='cdp-sidebar')
    main = Main(class_name="cdp-content")
    support = Component(class_name="support")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert self.menu.is_visible

                return self.main.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()
