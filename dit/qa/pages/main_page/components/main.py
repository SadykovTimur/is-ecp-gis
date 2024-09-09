from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    title = Text(tag='h3')
    info = Component(xpath='//h4[text()=" Информационные системы  "] ')
    links = Component(xpath='//h4[text()=" Быстрые ссылки  "] ')
    news = Component(xpath='//h4[text()=" Новости  "] ')
    registry = Component(xpath='//h4[contains(text(),"Реестров в избранном")]')
    favorites = Component(xpath='//h4[contains(text(),"Возможностей в избранном")]')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'Здравствуйте, Функц Мониторинг!'
        assert self.info.visible
        assert self.links.visible
        assert self.news.visible
        assert self.registry.visible

        return self.favorites.visible


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
