from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Menu']


class LayersWrapper(ComponentWrapper):
    mayors_instructions = Component(xpath='//span[text()="Поручения Мэра"]')
    control_orders = Component(
        xpath='//span[text()="Контрольные поручения"]//preceding-sibling::gis-plugin-navigator-checkbox')
    video_cameras = Component(xpath='//span[text()="Камеры видеонаблюдения"]')
    contract_cameras = Component(xpath='//span[text()="Контрактные камеры"]')
    public_places = Component(
        xpath='//span[text()="Общественные места (упр., HD)"]//preceding-sibling::gis-plugin-navigator-checkbox')


class Layers(Component):
    def __get__(self, instance, owner) -> LayersWrapper:
        return LayersWrapper(instance.app, self.find(instance), self._locator)


class MenuWrapper(ComponentWrapper):
    interface = Component(css='[class*="icon-alt-map"]')
    orthophoto = Component(css='[class*="orto"]')
    layers = Layers(tag='gis-plugin-layers-tree-tab')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
