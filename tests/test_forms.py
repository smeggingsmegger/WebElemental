import sys
from datetime import datetime

from HttpBase import HttpBase


class TestForms(HttpBase):

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.elemental.screenshot(test_method_name + "-" + now + ".png")

    def test_fill_form(self):
        self.elemental.goto('/tests/html/forms.html')
        self.elemental.wait_for_visible('#textfield')

        self.elemental.set_value('#textfield', 'This is a test')
        self.elemental.set_value('#selectfield', '3')
        self.elemental.wait_for_text_in_value('#textfield', 'This is a test')
        self.elemental.wait_for_text_in_value('#selectfield', '3')
        assert self.elemental.get_value('#textfield') == 'This is a test'
        assert self.elemental.get_value('#selectfield') == '3'
        # We have to clear the text field when using fill
        self.elemental.clear('#textfield')
        self.elemental.fill({
            '#textfield': 'Booya!',
            '#selectfield': 'Four'
        })
        self.elemental.wait_for_text_in_value('#textfield', 'Booya!')
        self.elemental.wait_for_text_in_value('#selectfield', '4')
        assert self.elemental.get_value('#textfield') == 'Booya!'
        assert self.elemental.get_value('#selectfield') == '4'
        self.elemental.set_value('#textfield', 'No clear needed')
        self.elemental.wait_for_text_in_value('#textfield', 'No clear needed')
        assert self.elemental.get_value('#textfield') == 'No clear needed'

        # Test set_values:

        # Dict:
        self.elemental.set_values({
            '#textfield': 'AAAAAAAA',
            '#selectfield': '5'
        })
        self.elemental.wait_for_text_in_value('#textfield', 'AAAAAAAA')
        self.elemental.wait_for_text_in_value('#selectfield', '5')
        assert self.elemental.get_value('#textfield') == 'AAAAAAAA'
        assert self.elemental.get_value('#selectfield') == '5'

        # List of list:
        self.elemental.set_values([
            ['#textfield', 'BBBBBBBB'],
            ['#selectfield', '6']
        ])
        self.elemental.wait_for_text_in_value('#textfield', 'BBBBBBBB')
        self.elemental.wait_for_text_in_value('#selectfield', '6')
        assert self.elemental.get_value('#textfield') == 'BBBBBBBB'
        assert self.elemental.get_value('#selectfield') == '6'

        # List of Mix:
        self.elemental.set_values([
            ('#textfield', 'CCCCCCCC'),
            {'#selectfield': '7'}
        ])
        self.elemental.wait_for_text_in_value('#textfield', 'CCCCCCCC')
        self.elemental.wait_for_text_in_value('#selectfield', '7')
        assert self.elemental.get_value('#textfield') == 'CCCCCCCC'
        assert self.elemental.get_value('#selectfield') == '7'

    def test_screenshot(self):
        import os.path
        path = '/tmp/selenium-screenshot.png'
        self.elemental.screenshot()
        assert os.path.isfile(path)
        assert os.path.getsize(path) > 0
