from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['TopButtons']


class TopButtonsWrapper(ComponentWrapper):
    measure = Button(css='[class*="ruler"]')
    measure_distance = Button(css='button [class*="line"]')
    measure_square = Button(css='button [class*="rectangle"]')
    measure_perimeter = Button(css='button [class*="polygon"]')
    panorams = Button(css='[class*="pedestrian"]')


class TopButtons(Component):
    def __get__(self, instance, owner) -> TopButtonsWrapper:
        return TopButtonsWrapper(instance.app, self.find(instance), self._locator)
