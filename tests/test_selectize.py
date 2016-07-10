from HttpBase import HttpBase


class TestSelectize(HttpBase):

    def test_set_selectize_basic(self):
        self.elemental.goto('/tests/html/selectize.html')
        select_el = '#testSelectize'
        test_value = 'Option 2'
        self.elemental.wait_for_visible(select_el + ' + .selectize-control')
        self.elemental.set_selectize(select_el, test_value)
        assert self.elemental.get_value(select_el) == test_value

    def test_set_selectize_async(self):
        self.elemental.goto('/tests/html/selectize.html?async=true')
        select_el = '#testSelectize'
        test_value = 'Option 3'
        self.elemental.wait_for_visible(select_el + ' + .selectize-control')
        self.elemental.set_selectize(select_el, test_value)
        assert self.elemental.get_value(select_el) == test_value
