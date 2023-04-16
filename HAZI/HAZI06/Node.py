class Node():
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, info_gain=None, value=None): 
        self.value = value
        self.threshold = threshold
        self.left = left
        self.feature_index = feature_index
        self.right = right
        self.info_gain = info_gain 