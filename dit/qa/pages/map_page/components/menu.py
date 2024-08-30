from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    interface = Component(css='[class*="icon-alt-map"]')
    orthophoto = Component(css='[class*="orto"]')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
