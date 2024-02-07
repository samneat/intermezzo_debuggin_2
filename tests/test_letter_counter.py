from lib.letter_counter import *

def test_with_digital_punk_string():
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]

def test_with_random_string():
    counter = LetterCounter("eaegbphada")
    assert counter.calculate_most_common() == [3, "a"]