from abc import ABCMeta, abstractmethod
from Snap import Snap
from math import *

# Class to hold info regarding slices of the object
# created from two pictures. i.e. Snap class.
# Base class for various calculation possibilities.

class Slice(object):
    __metaclass__ = ABCMeta
    
    # Variable Declaration #
    _snapOne = None
    _snapTwo = None
    _angle = 0
    
    def __init__(self, snapOne, snapTwo, angle):
        if not self.setSnapOne(snapOne):
            self._snapOne = Snap()
        if not self.setSnapTwo(snapTwo):
            self._snapTwo = Snap()
        if not self.setAngle(angle):
            self_angle = 0

    @abstractmethod
    def getAreaOne(self):
        pass

    @abstractmethod
    def getAreaTwo(self):
        pass
    
    # Property Mutators #
    def setAngle(self, angle):
        if angle is  None:
            return false
        self._angle = angle
        return True

    def getAngle(self):
        return self._angle
    
    def setSnapOne(self, snap):
        if self._snapTwo is not None:
            if self._snapTwo.levels != snap.levels:
                return False
        else:
            return False

        self._snapOne = snap
        return True

    def setSnapTwo(self, snap):
        if self._snapOne is not None:
             if self._snapOne.levels != snap.levels:
                return False
        else:
            return False
        
        self._snapTwo = snap
        return True

    def getSnapOne(self):
        return self._snapOne

    def getSnapTwo(self):
        return self._snapTwo

    # Property Declaration Variables
    angle = property(getAngle, setAngle, "Var. to hold angle between Snaps.")
    snapOne = property(getSnapOne, setSnapOne, "Holds the first Snap.")
    snapTwo = property(getSnapTwo, setSnapTwo, "Holds the second Snap.")

class BlockSlice(Slice):
    
    def __init__(self, snapOne = Snap(), snapTwo = Snap(), angle = 0.0):
        super(BlockSlice, self).__init__(snapOne, snapTwo, angle)

    # Calculates Area One
    def getAreaOne(self):
        leftPoints = []
        rightPoints = []
        for points in self.snapOne.dataPoints:
            leftPoints.append(points.right)
        for points in self.snapTwo.dataPoints:
            rightPoints.append(points.right)
        height = self.getHeight()
        return self.calculateArea(leftPoints, rightPoints, height)

    # Calculates Area Two
    def getAreaTwo(self):
        leftPoints = []
        rightPoints = []
        for points in self.snapOne.dataPoints:
            leftPoints.append(points.left)
        for points in self.snapTwo.dataPoints:
            rightPoints.append(points.left)
        height = self.getHeight()
        return self.calculateArea(leftPoints, rightPoints, height)

    # Calculates the Height of the Slice and returns it
    def getHeight(self):
        height = self.snapOne.calcMaxHeight()
        otherHeight = self.snapTwo.calcMaxHeight()
        if(height < otherHeight):
            height = otherHeight 
        return height
            
    def calculateArea(self, leftDataPoints, rightDataPoints, height):
        numPoints = len(leftDataPoints)
        result = 0.0
        for x in range(0, numPoints):
            lVal = leftDataPoints[x]
            rVal = rightDataPoints[x]
            deltaH = height/numPoints
            lCosOne = pow(lVal, 2)+ pow(rVal, 2)
            result += deltaH * sqrt( lCosOne - (2*lVal*rVal*cos(radians(self._angle))))
        return result
