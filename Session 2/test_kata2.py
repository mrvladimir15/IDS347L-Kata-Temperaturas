import pytest
from KataTemperatures2 import Temperature

class TestTemp2():
    Temperature = 25
    Scale = "C"
    
    def test_t1(self):
        assert Temperature.Add(self, 5, "F") == 10
    
    def test_t2(self):
        assert Temperature.Substract(self, 5, "K") == -233.15
    
    def test_t3(self):
        assert Temperature.MultiplyBy(self, 4, "C") == 100
    
    def test_t4(self):
        assert Temperature.DivideBy(self, 32, "F") == "Error! Cannot divide by zero"
    
    def test_t5(self):
        assert Temperature.DivideBy(self, 293.15, "K") == 1.25
    
    def test_t6(self):
        assert Temperature.ToString() == "25C"