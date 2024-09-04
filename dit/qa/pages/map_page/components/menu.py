from coms.qa.frontend.pages.component import Component, ComponentWrapper, Components

__all__ = ['Menu']

from coms.qa.frontend.pages.component.text_field import TextField


class LayersWrapper(ComponentWrapper):
    mayors_instructions = Component(xpath='//span[text()="Поручения Мэра"]')
    control_orders = Component(
        xpath='//span[text()="Контрольные поручения"]//preceding-sibling::gis-plugin-navigator-checkbox')

    video_cameras = Component(xpath='//span[text()="Камеры видеонаблюдения"]')
    contract_cameras = Component(xpath='//span[text()="Контрактные камеры"]')
    public_places = Component(
        xpath='//span[text()="Общественные места (упр., HD)"]')
    broadcast_is_on = Component(
        xpath='//span[text()="Идет трансляция"]//preceding-sibling::gis-plugin-navigator-checkbox')

    aerial_photography = Component(xpath='//span[text()="Аэросъёмка"]')
    bpla_video = Component(xpath='//span[text()="Видео с БПЛА"]//preceding-sibling::gis-plugin-navigator-checkbox')
    bpla_panoramas = Component(
        xpath='//span[text()="Панорамы 360 с БПЛА"]//preceding-sibling::gis-plugin-navigator-checkbox')


class Layers(Component):
    def __get__(self, instance, owner) -> LayersWrapper:
        return LayersWrapper(instance.app, self.find(instance), self._locator)


class MenuWrapper(ComponentWrapper):
    interface = Component(css='[class*="icon-alt-map"]')
    orthophoto = Component(css='[class*="orto"]')
    layers = Layers(tag='gis-plugin-layers-tree-tab')
    search = TextField(xpath='//input[@placeholder="Поиск"]')
    address = Components(xpath='//b[text()="Город Москва, Красная площадь, дом 1"]')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
