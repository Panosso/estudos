from count_bits import count_bits
from letter_value_excel_sheet import title_to_number
from square_of_square import is_square
from high_and_low import high_and_low
from sum_digits import digital_root

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

    def test_square_of_square(self):
        assert is_square(-1) == False
        assert is_square( 0) == True
        assert is_square( 3) == False
        assert is_square( 4) == True
        assert is_square(25) == True
        assert is_square(26) == False
        assert is_square(36) == True

    def test_high_and_low(self):
        assert high_and_low("1 2 3 4 5") == "5 1"
        assert high_and_low("1 2 -3 4 5") == "5 -3"
        assert high_and_low("1 9 3 4 -5") == "9 -5" 

    def test_digital_root(self):
        assert digital_root(16) == 7
        assert digital_root(942) == 6
        assert digital_root(132189) == 6
        assert digital_root(493193) == 2