from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    title = Text(id="sidebar_system-name")
    gos_function = Component(xpath='//div[text()=" Госуслуги и функции "]')
    info = Component(xpath='//div[text()=" Информация "]')
    settings = Component(xpath='//div[text()=" Настройки "]')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'Правительство Москвы'
        assert self.gos_function.visible
        assert self.info.visible

        return self.settings.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
