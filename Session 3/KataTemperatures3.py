class Temperature():
    
    # Constructor
    def __init__(self, Temperature, Scale):
        self.Temperature = Temperature
        self.Scale = Scale
    
    # Prints scale
    def GetScale(self):
        return self.Scale
    
    # Prints temperature's value and scale
    def ToString(self):
        return self.Temperature, self.Scale
    
    ### Begin of Conversions
    def ToCelsius(self):
        if self.Scale != "C":
            if self.Scale == "F":
                return (self.Temperature-32)/1.8
            elif self.Scale == "K":
                return self.Temperature - 273.15
            else:
                return "Invalid scale"
        else:
            return self.Temperature
    
    def ToFahrenheit(self):
        if self.Scale != "F":
            if self.Scale == "C":
                return (self.Temperature*1.8)+32
            elif self.Scale == "K":
                return self.Temperature*1.8 - 459.67
            else:
                return "Invalid scale"
        else:
            return self.Temperature
    
    def ToKelvin(self):
        if self.Scale != "K":
            if self.Scale == "C":
                return self.Temperature+273.15
            elif self.Scale == "F":
                return (self.Temperature-32)/1.8+273.15
            else:
                return "Invalid scale"
        else:
            return self.Temperature
    ### End of Conversions
    
    ### Begin of Operations
    def Add(self, temp2, scale2):
        if self.Scale == "C":
            newValue = Temperature(temp2, scale2).ToCelsius()
        elif self.Scale == "F":
            newValue = Temperature(temp2, scale2).ToFahrenheit()
        elif self.Scale == "K":
            newValue = Temperature(temp2, scale2).ToKelvin()
        else:
            return "Invalid scale"
        
        return self.Temperature + newValue
    
    def Substract(self, temp2, scale2):
        if self.Scale == "C":
            newValue = Temperature(temp2, scale2).ToCelsius()
        elif self.Scale == "F":
            newValue = Temperature(temp2, scale2).ToFahrenheit()
        elif self.Scale == "K":
            newValue = Temperature(temp2, scale2).ToKelvin()
        else:
            return "Invalid scale"
        return self.Temperature - newValue
    
    def MultiplyBy(self, tmep2, scale2)        :
        if self.Scale == "C":
            newValue = Temperature(temp2, scale2).ToCelsius()
        elif self.Scale == "F":
            newValue = Temperature(temp2, scale2).ToFahrenheit()
        elif self.Scale == "K":
            newValue = Temperature(temp2, scale2).ToKelvin()
        else:
            return "Invalid scale"
        return self.Temperature * newValue
    
    def DivideBy(self, temp2, scale2):
        if self.Scale == "C"        :
            newValue = Temperature(temp2, scale2).ToCelsius()
        elif self.Scale == "F":
            newValue = Temperature(temp2, scale2).ToFahrenheit()
        elif self.Scale == "K":
            newValue = Temperature(temp2, scale2).ToKelvin()
        else:
            return "Invalid scale"
        
        if newValue != 0:
            return self.Temperature / newValue
        else:
            return "Cannot divide by zero!"
    ### End of Operations