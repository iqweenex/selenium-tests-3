import pytest
from pages.infinity_scroll.infinity_scroll_page import InfinityScrolPage
from utils.logger import Logger


class TestInfinityScroll:
    URL = "http://the-internet.herokuapp.com/infinite_scroll"

    @pytest.mark.parametrize("target_count", [27])
    def test_infinity_scroll(self, browser, target_count):
        Logger.info(f"Тест infinity scroll - количество абзацев: {target_count}")

        scroll_page = InfinityScrolPage(browser)
        browser.get(self.URL)
        scroll_page.wait_for_open()

        current_count = 0
        max_attempts = 120

        for attempt in range(max_attempts):
            current_count = scroll_page.get_paragraphs_count()

            if current_count >= target_count:
                Logger.info(f"Достигнуто количество абзацев {current_count}\n"
                            f"Понадобилось {attempt} прокруток")
                break
            browser.scroll_to_bottom()
        else:
            raise AssertionError(f"После {max_attempts} необходимое количество {target_count} не достигнуто")

        assert current_count >= target_count, f"Ожидаемое количество {target_count}\n" \
                                              f"Достигнутое количество {current_count}"

        Logger.info(f"Тест Infinity Scroll завершен успешно")
