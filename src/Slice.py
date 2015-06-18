from DataPoint import DataPoint

class Slice(object):
    # Collection of datapoints.
    _dataPoints = []
    
    def __init__(self, levels = 1 ):
        if not self.setLevels(levels):
            self._levels = 1
            
    # Pops the last added point in the list.
    def pop(self):
        if len(self._dataPoints) < 0:
            return false
        self._dataPoints.pop()
        return true

    # Adds a set of point values to the program.
    def push(self, dataPoint):
        if len(self._dataPoints) >= self._levels:
            return False
        self._dataPoints.append(dataPoint)
        return True

    # Overloaded function for push.
    def addPoint(self, dataPoint):
        return self.push(dataPoint)
    
    # Properties functions.
    def getDataPoints(self):
        return self._dataPoints

    dataPoints = property(getDataPoints, "Variable to hold all the points of data in slice.")
    
    def setLevels(self, levels):
        if levels < 0:
            levels = -levels
        self._levels = levels
        return True

    def getLevels(self):
        return self._levels

    # Public Property Declration for _levels
    levels = property(getLevels, setLevels, "Indicates the number of points on the canvas")
    
    # Print overrides
    def __str__(self):
        result = "[";
        indexSize = len(self._dataPoints) - 1;

        if indexSize < 0:
            return result + "]"
        
        for x in range (0, indexSize):
            result += self._dataPoints[x].__str__() + ";"
            
        result += self._dataPoints[indexSize].__str__() + "]"
        return result
