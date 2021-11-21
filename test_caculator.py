"""
Unit tests for the calculator library
"""

import calculator

class TestCalculator:

   def test_addition(self):
        assert 4 == calculator.add(2, 2)

   def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

   def test_multiply(self):
    assert 100 == calculator.multiply(10, 10)

   def test_divide(self):
   	assert 81 == calculator.divide(243, 3)

