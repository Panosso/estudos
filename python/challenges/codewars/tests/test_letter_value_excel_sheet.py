from letter_value_excel_sheet import title_to_number
from count_bits import count_bits

class TestClass:

    def test_letter_value_excel_sheet(self):
        assert title_to_number('A') == 1
        assert title_to_number('Z') == 26
        assert title_to_number('AA') == 27
        assert title_to_number('BA') == 53
        assert title_to_number('AAA') == 703
        assert title_to_number('CODEWARS') == 28779382963
        assert title_to_number('PEDRO') == 7402683

    def test_count_bit(self):

        assert count_bits(0) == 0
        assert count_bits(1) == 1
        assert count_bits(4) == 1
        assert count_bits(7) == 3
        assert count_bits(9) == 2
        assert count_bits(10) == 2
        assert count_bits(15) == 4
