from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['RightButtons']


class RightButtonsWrapper(ComponentWrapper):
    initial_position = Button(css='[class*="base-screen"]')
    zoom_in = Button(css='[class*="plus"]')
    zoom_out = Button(css='[class*="minus"]')
    zoom_value = Text(css='[class*="value"]')
    orientation = Button(css='gis-plugin-compass-button svg')

    @property
    def rotate(self) -> str:
        return self.orientation.webelement.get_attribute('style')


class RightButtons(Component):
    def __get__(self, instance, owner) -> RightButtonsWrapper:
        return RightButtonsWrapper(instance.app, self.find(instance), self._locator)
