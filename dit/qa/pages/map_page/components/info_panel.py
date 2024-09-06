from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['InfoPanel']


class InfoPanelWrapper(ComponentWrapper):
    menu = Button(css='[class*="card-menu"]')
    to_object = Button(css='[class*="to-object"]')
    object_card = Button(css='[class*="object-description"]')
    csv_file = Button(css='[class*="csv-file"]')

    @property
    def is_visible(self) -> bool:
        assert self.to_object.visible
        assert self.object_card.visible

        return self.csv_file.visible


class InfoPanel(Component):
    def __get__(self, instance, owner) -> InfoPanelWrapper:
        return InfoPanelWrapper(instance.app, self.find(instance), self._locator)
