from Slice import *

# Class to calculate volume of the object
# and manage the multiple slices of an object.
# Slices should be loaded and given by a loader.

class Volume(object):
    _slices = []

    def __init__(self, slices):
        if not self.setSlices(slices):
            test = Snap(2)
            test.addPoint(DataPoint(0, 1, 1))
            test.addPoint(DataPoint(1, 1, 1)) 
            self._slices.append(BlockSlice(test, test, 90));
            
            self._slices.append(BlockSlices())
            self._slices.append
