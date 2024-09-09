from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException


__all__ = ['InstructionsObjectCardPage']


class InstructionsObjectCardPage(Page):
    header = Component(css='[class*="cdp-navbar"]')
    menu = Component(id='side-menu')
    card_header = Component(tag='instruction-card-header')
    tabs = Component(css='[class*="tabs"]')
    order_type = Component(xpath='//span[text()="Контрольное поручение Мэра Москвы"]')
    content = Component(css='[class*="clearfix "]')
    footer = Component(class_name="footer")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.menu.visible
                assert self.card_header.visible
                assert self.tabs.visible
                assert self.order_type.visible
                assert self.content.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Карточка объекта "Контрольные поручения" не загружена')
        self.app.restore_implicitly_wait()
