from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    nav = Component(id="nav-header")
    title_header = Component(xpath='//a[text()=" Иванов Функц Мониторинг "]')
    logout = Component(css='[class*="sign-out"]')
    bell = Component(css='[class*="bell"]')
    wrench = Component(css='[class*="wrench"]')
    cogs = Component(css='[class*="cogs"]')

    @property
    def is_visible(self) -> bool:
        assert self.nav.visible
        assert self.title_header.visible
        assert self.logout.visible
        assert self.bell.visible
        assert self.wrench.visible

        return self.cogs.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
