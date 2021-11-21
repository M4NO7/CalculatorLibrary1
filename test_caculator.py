"""
Unit tests for the calculator library
"""

import caculator

class TestCaculator:

   def test_addition(self):
        assert 4 == caculator.add(2, 2)

   def test_subtract(self):
        assert 2 == caculator.subtract(4, 2)

   def test_multiply(self):
    assert 100 == caculator.multiply(10, 10)

   def test_divide(self):
   	assert 81 == caculator.divide(243, 3)

   def test_powerof(self):
   	assert 169 == caculator.powerof(13, 13)
