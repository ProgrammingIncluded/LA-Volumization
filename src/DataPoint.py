class DataPoint(object):
    def __init__(self, height = 0.0, left = 0.0, right = 0.0):
        self.height = float(height)
        self.left = float(left)
        self.right = float(right)
        
    def __str__(self):
        return "(%f, %f, %f)" % (self.height, self.left, self.right)
