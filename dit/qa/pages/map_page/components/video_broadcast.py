from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['VideoBroadcast']


class VideoBroadcastWrapper(ComponentWrapper):
    close = Button(css='[title="Закрыть"]')


class VideoBroadcast(Component):
    def __get__(self, instance, owner) -> VideoBroadcastWrapper:
        return VideoBroadcastWrapper(instance.app, self.find(instance), self._locator)
