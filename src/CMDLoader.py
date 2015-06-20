from Volume import BlockVolume
from Snap import Snap
from DataPoint import DataPoint

# Class with helping input data in CMD.
class CMDLoader:
    _numSnaps = 0
    _numLevels = 0
    _volume = BlockVolume()
    _prevHeight = None

    # Snaps should be even
    def __init__(self, numSnaps = 2, numLevels = 2):
        if numSnaps % 2 != 0:
            numSnaps += 1
        self. _numSnaps = numSnaps
        self._numLevels = numLevels

    def displayDataInput(self):
        print "\nData Parsed:\n"
        slices = self._volume.slices
        for slice in slices:
            print slice.snapOne
            print slice.snapTwo
        
    def displayResult(self):
        print "\nYour volume is..."
        print self._volume.calculateVolume()

    def inputInfo(self):
        snapOne = None
        snapTwo = None
        for x in range(0, self._numSnaps):
            print "\nPlease enter picture %i info.:\n" %(x+1)
            leftData = self.inputFirstSnapPoints()
            rightData = self.inputSecondSnapPoints()
            if x % 2 != 0:
                snapOne = Snap(self._numLevels)
                for i in range(0, len(rightData)):
                    snapOne.addPoint(DataPoint(self._prevHeight[i], leftData[i], rightData[i]))
            else:
                snapTwo = Snap(self._numLevels)
                for i in range(0, len(rightData)):
                    snapTwo.addPoint(DataPoint(self._prevHeight[i], leftData[i], rightData[i]))
                self._volume.createSlice(snapOne, snapTwo, 180/self._numSnaps)
            
    def inputFirstSnapPoints(self):
        leftData = []
        self._prevHeight = []
        print "Enter left points with height values. i.e. height, left"
        for x in range(0, self._numLevels):
            input = raw_input("Point " + str(x) + ": ")
            values = self.parseInput(input)
            self._prevHeight.append(values[0])
            leftData.append(values[1])
        return leftData
            
    def inputSecondSnapPoints(self):
        rightData = []
        print "Enter right points without height. i.e. right"
        for x in range(0, self._numLevels):
            input = raw_input("Point " + str(x) + " Height "  + str(self._prevHeight[x]) + ": ")
            values = self.parseInput(input)
            rightData.append(values[0])
        return rightData
        
    def parseInput(self, input):
        values = [result.strip() for result in input.split(",")]
        numbers = []
        if len(values) == 2:
            numbers = [int(values[0]), int(values[1])]
        elif len(values) == 1:
            numbers = [int(values[0])]
        else:
            numbers = [0,0,0]
        return numbers
