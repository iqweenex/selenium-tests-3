from typing_extensions import Self

from browser.browser import Browser
from elements.web_element import WebElement


class MultiWebElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int = None
    ) -> None:
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else self.formattable_xpath.format("'i'")

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = self.get_by_index(self.index)
        if not current_element.is_exist():
            raise StopIteration
        self.index += 1
        return current_element

    def __len__(self) -> int:
        count = 0
        for _ in self:
            count += 1
        return count

    def get_by_index(self, index: int) -> WebElement:
        return WebElement(
            self.browser,
            self.formattable_xpath.format(index),
            f"{self.description}[{index}]",
            self.timeout
        )
