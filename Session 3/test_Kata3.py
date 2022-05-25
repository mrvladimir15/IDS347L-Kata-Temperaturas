import pytest
from KataTemperatures3 import Temperature

class testKata3():
    Temperature = 45
    Scale = "C"
    
    # Add
    def test_t1(self):
        assert Temperature.Add(self, 45, "C") == 90
    
    def test_t2(self):
        assert Temperature.Add(self, 45, "K") == -183.15
    
    def test_t3(self):
        assert Temperature.Add(self, 400, "F") == 249.4444
    
    # Substract
    def test_t4(self):
        assert Temperature.Substract(self, 45, "C") == 0
    
    def test_t5(self):
        assert Temperature.Substract(self, 45, "K") == 273.15
    
    def test_t6(self):
        assert Temperature.Substract(self, 400, "F") == -159.4444
    
    # MultiplyBy
    def test_t7(self):
        assert Temperature.MultiplyBy(self, 45, "C") == 2025
    
    def test_t8(self):
        assert Temperature.MultiplyBy(self, 45, "K") == -10,266.75
    
    def test_t9(self):
        assert Temperature.MultiplyBy(self, 14, "F") == -450
    
    # DivideBy
    def test_t10(self):
        assert Temperature.DivideBy(self, 45, "C") == 1
    
    def test_t11(self):
        assert Temperature.DivideBy(self, 283.15, "K") == 4.5
    
    def test_t12(self):
        assert Temperature.DivideBy(self, 14, "F") == -4.5
    
    def test_t13(self):
        assert Temperature.DivideBy(self, 0, "C") == "Cannot divide by zero!"
    
    def test_t14(self):
        assert Temperature.ToString(self) == (45, "C")
    
    def test_t15(self):
        assert Temperature.ToScale(self) == "C"