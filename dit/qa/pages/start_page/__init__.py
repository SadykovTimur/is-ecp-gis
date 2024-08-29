from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    logo = Component(css='[class*="logo"]')
    title = Text(tag='h1')
    login_title = Button(css='[class*="title_login"]')
    footer = Component(class_name='login-page-footer')
    login = TextField(id="username")
    password = TextField(id="password")
    submit = TextField(id="kc-login")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title == 'Правительство Москвы'
                assert self.login_title.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Стартовая страница не загружена')
        self.app.restore_implicitly_wait()
