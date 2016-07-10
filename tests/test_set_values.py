from HttpBase import HttpBase


class TestForms(HttpBase):

    def test_fill_form(self):
        self.elemental.goto('/tests/html/forms.html')
        self.elemental.wait_for_visible('#textfield')
        self.elemental.set_value('#textfield', 'This is a test')
        self.elemental.set_value('#selectfield', '3')
        assert self.elemental.get_value('#textfield') == 'This is a test'
        assert self.elemental.get_value('#selectfield') == '3'
        # We have to clear the text field when using fill
        self.elemental.clear('#textfield')
        self.elemental.fill({
            '#textfield': 'Booya!',
            '#selectfield': 'Four'
        })
        assert self.elemental.get_value('#textfield') == 'Booya!'
        assert self.elemental.get_value('#selectfield') == '4'
        self.elemental.set_value('#textfield', 'No clear needed')
        assert self.elemental.get_value('#textfield') == 'No clear needed'

