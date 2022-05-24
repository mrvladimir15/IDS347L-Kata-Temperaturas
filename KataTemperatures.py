class Temperature():
    
    # Constructor
    def __init__(self, Temperature, Scale):
        self.Temperature = Temperature
        self.Scale = Scale
    
    # Prints the temperature's value and its scale
    def ToString(self):
        return self.Temperature, " ", self.Scale
    
    # Prints the temperature's scale
    def GetScale(self):
        return self.Scale
    
    ### Begin of Conversions
    def ToCelsius(self):
        if self.Scale != "C":
            # F->C
            if self.Scale == "F":
                return (self.Temperature - 32)/1.8
            # K->C
            elif self.Scale == "K":
                return self.Temperature - 273.15
            else:
                return "Invalid scale."
        else:
            return self.Temperature
    
    def ToFahrenheit(self):
        if self.Scale != "F":
            # C->F
            if self.Scale == "C":
                return (self.Temperature * 1.8) + 32
            # K->F
            elif self.Scale == "K":
                return self.Temperature*1.8-459.67
        else:
            return self.Temperature

    def ToKelvin(self):
        if self.Scale != "K":
            # F->K
            if self.Scale == "F":
                return (self.Temperature-32)/1.8 + 273.15
            # C->K
            elif self.Scale == "C":
                return self.Temperature + 273.15
        else:
            return self.Temperature
    ### End of Conversions
    
    ### Begin of operations
    def Add(self, temp2, scale2):
        # Celsius degrees
        if self.Scale == "C":
            convertedValue = Temperature(temp2, scale2).ToCelsius()
            return self.Temperature + convertedValue
        # Fahrenheit degrees
        elif self.Scale == "F":
            convertedValue = Temperature(temp2, scale2).ToFahrenheit()
            return self.Temperature + convertedValue
        # Kelvin degrees
        elif self.Scale == "K":
            convertedValue = Temperature(temp2,scale2).ToKelvin()
            return self.Temperature + convertedValue
        else:
            return "Invalid scale"
    
    def Substract(self, temp2, scale2):
        # Celsius degrees
        if self.Scale == "C":
            convertedValue = Temperature(temp2, scale2).ToCelsius()
            return self.Temperature - convertedValue
        # Fahrenheit degrees
        elif self.Scale == "F":
            convertedValue = Temperature(temp2, scale2).ToFahrenheit()
            return self.Temperature - convertedValue
        # Kelvin degrees
        elif self.Scale == "K":
            convertedValue = Temperature(temp2, scale2).ToKelvin()
            return self.Temperature - convertedValue
        else:
            return "Invalid scale"
    
    def MultiplyBy(self, temp2, scale2):
        # Celsius degrees
        if self.Scale == "C":
            convertedValue = Temperature(temp2, scale2).ToCelsius()
            return self.Temperature * convertedValue
        # Fahrenheit degrees
        elif self.Scale == "F":
            convertedValue = Temperature(temp2, scale2).ToFahrenheit()
            return self.Temperature * convertedValue
        # Kelvin degrees
        elif self.Scale == "K":
            convertedValue = Temperature(temp2, scale2).ToKelvin()
            return self.Temperature * convertedValue
        else:
            return "Invalid scale"
    
    def DivideBy(self, temp2, scale2):
        if temp2 != 0:
            # Celsius degrees
            if self.Scale == "C":
                convertedValue = Temperature(temp2, scale2).ToCelsius()
                return self.Temperature/convertedValue
            # Fahrenheit degrees
            elif self.Scale == "F":
                convertedValue = Temperature(temp2, scale2).ToFahrenheit()
                return self.Temperature/convertedValue
            # Kelvin degrees
            elif self.Scale == "K":
                convertedValue = Temperature(temp2, scale2).ToKelvin()
                return self.Temperature/convertedValue
            else:
                return "Invalid scale"
        else:
            return "Cannot divide by zero"
    ### End of operations
    
a = Temperature(25, "C")
b = Temperature(5, "F")

print (a.MultiplyBy(b.Temperature, b.Scale))