class DataPoint(object):
    def __init__(self, height = 0, left = 0, right = 0):
        self.height = height
        self.left = left
        self.right = right
        
    def __str__(self):
        return "(%i, %i, %i)" % (self.height, self.left, self.right)
