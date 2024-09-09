from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['BplaObjectCardPage']


class BplaObjectCardPage(Page):
    loader = Component(css='[class*="ui-spin"]')
    header = Component(tag='cdp-navbar')
    menu = Component(tag='cdp-sidebar')
    title = Text(tag='h1')
    info = Component(css='[class*="card__info"]')
    media = Component(css='[class*="card__media"]')
    footer = Component(tag='cdp-footer')
    video_player = Component(tag='app-custom-player')
    controls = Component(css='[class*="controls"]')
    play = Button(css='[class*="start"]')
    time = Text(tag='time')

    @property
    def loader_is_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    @staticmethod
    def video_playback(start_time: str, end_time: str) -> None:
        try:
            assert end_time > start_time

        except AssertionError as e:
            raise AssertionError('При воспроизведении видео возникла ошибка') from e

    def wait_for_loading_bpla_video(self) -> None:
        def condition() -> bool:
            try:
                assert self.loader_is_hidden
                assert self.header.visible
                assert self.menu.visible
                assert "Технический номер заявки" in self.title
                assert self.info.visible
                assert self.media.visible
                assert self.video_player.visible
                assert self.controls.visible
                assert self.play.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=100, msg='Карточка объекта "Видео с БПЛА" не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_bpla_panoramas(self) -> None:
        def condition() -> bool:
            try:
                assert self.loader_is_hidden
                assert self.header.visible
                assert self.menu.visible
                assert "Технический номер заявки" in self.title
                assert self.info.visible
                assert self.media.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=100, msg='Карточка объекта "Панорамы 360 с БПЛА" не загружена')
        self.app.restore_implicitly_wait()
