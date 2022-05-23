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
    def ToCelsius(tempValue, tempScale):
        if tempScale != "C":
            # F->C
            if tempScale == "F":
                return (tempValue - 32)/1.8
            # K->C
            elif tempScale == "K":
                return tempValue - 273.15
            else:
                return "Invalid scale."
        else:
            return tempValue
    
    def ToFahrenheit(tempValue, tempScale):
        if tempScale != "F":
            # C->F
            if tempScale == "C":
                return (tempValue * 1.8) + 32
            # K->F
            elif tempScale == "K":
                return tempValue*1.8-459.67
        else:
            return tempValue

    def ToKevin(tempValue, tempScale):
        if tempScale != "K":
            # F->K
            if tempScale == "F":
                return (tempValue-32)/1.8 + 273.15
            # C->K
            elif tempScale == "C":
                return tempValue + 273.15
        else:
            return tempValue
    ### End of Conversions
    
    ### Begin of operations
    def Add(self, temp2, scale2):
        # Main class scale        
        mainScale = self.Scale
        
        if mainScale == "C":
            if scale2 == "F":
                Temperature()
            elif scale2 == "K:":
            else:
                return "Invalid scale"
    ### End of operations
    
a = Temperature(25, "C")
b = Temperature(5, "C")

print (a.Add(b.Temperature))