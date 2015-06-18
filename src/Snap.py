from DataPoint import DataPoint

# Class to hold data for individual snap shot.
class Snap(object):
    # Collection of datapoints.
    _dataPoints = []
    
    def __init__(self, levels = 1 ):
        if not self.setLevels(levels):
            self._levels = 1

    def calcMaxHeight(self):
        size = len(self._dataPoints)
        if size <= 0:
            return 0.0
        elif  size == 1:
            return self._dataPoints[0].height
        minVal = self._dataPoints[0].height
        maxVal = self._dataPoints[1].height

        if(minVal > maxVal):
            temp = maxVal
            maxVal = minVal
            minVal = temp

        for points in self._dataPoints:
            if(points.height > maxVal):
                maxVal = points.height
            elif(points.height < minVal):
                minVal = points.height

        return maxVal - minVal
            
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
    
    def setLevels(self, levels):
        if levels < 0:
            levels = -levels
        self._levels = levels
        return True

    def getLevels(self):
        return self._levels
 
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

    # Property Declaration Variables
    levels = property(getLevels, setLevels, "Indicates the number of points on the canvas")
    dataPoints = property(getDataPoints, "Variable to hold all the points in slice.")

