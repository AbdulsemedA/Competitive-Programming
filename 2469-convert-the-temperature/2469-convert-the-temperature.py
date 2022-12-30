class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = [celsius + 273.15]
        fahranheit = (celsius * 1.80) + 32.00
        result.append(fahranheit)
        
        return result
        