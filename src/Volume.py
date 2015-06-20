from abc import ABCMeta, abstractmethod
from Slice import *
from DataPoint import DataPoint

# Class to calculate volume of the object
# and manage the multiple slices of an object.
# Slices should be loaded and given by a loader.

class Volume(object):
    __metaclass__ = ABCMeta

    # Variable Declaration #
    _slices = []

    def __init__(self, slices):
        if not self.setSlices(slices):
            test = Snap(2)
            test.addPoint(DataPoint(0, 1, 1))
            test.addPoint(DataPoint(1, 1, 1)) 
            self._slices.append(BlockSlice(test, test, 90))            
            self._slices.append(BlockSlice(test, test, 90))
            self._slices.append

    # Abstract Functions #
    @abstractmethod
    def calculateVolume(self):
        pass
    
    # Function to call when you want to create slice
    # based on specific desired volume algorithm.
    @abstractmethod
    def createSlice(self, snapOne, snapTwo, angle):
        pass

    # Function to call when one wants to add generic slice
    # to Volume. Should be used internally by createSlice
    # to add slices.
    def addSlice(self, slice):
        if slice is None:
            return False
        if self._slices:
            firstSlice = self._slices[0]
            if firstSlice.angle != slice.angle:
                return False
            elif firstSlice.snapOne.levels != firstSlice.snapOne.levels:
                return False

        self._slices.append(slice)
        return True

    
    def setSlices(self, slices):
        if slices is None:
            return False
            
        self._slices = slices
        return True

    def getSlices(self):
        return self._slices

    # Property Declaration
    # Use with caution as you have to manually check the properties of the slices.
    slices = property(getSlices, setSlices, "List to hold of the slices")

    
# Class that calculates volume using block algorithm.
# Internally uses BlockSlice for individual Slice algorithm.
class BlockVolume(Volume):

    def __init__(self, slices = []):
        super(BlockVolume, self).__init__(slices)

    # Calculate the Volume.
    def calculateVolume(self):
        lSlices = self.slices
        if not lSlices:
            return 0.0
        # Get length of object.
        length = self.findLength(lSlices[0].snapOne.dataPoints)
        dLength = length / (len(lSlices) * 2)
        volume = 0.0
        for slice in lSlices:
            volume += (slice.getAreaOne() + slice.getAreaTwo()) * dLength
        return volume
        
    def createSlice(self, snapOne, snapTwo, angle):
        return self.addSlice(BlockSlice(snapOne,snapTwo, angle))

    # Get the lenght of the object.
    # Assumes DataPoint coordinates are from middle of image
    # as origin and all positive.
    def findLength(self, dataPoints):
        if dataPoints is None or not dataPoints:
            return 0.0
        leftPoints = []
        rightPoints = []

        for point in dataPoints:
            leftPoints.append(point.left)
            rightPoints.append(point.right)

        return self.findMax(leftPoints) + self.findMax(rightPoints)
            
    def findMax(self, values):
        if values is None or not values:
            return 0.0

        maxVal = values[0]
        for val in values:
            if maxVal < val:
                maxVal = val

        return maxVal
