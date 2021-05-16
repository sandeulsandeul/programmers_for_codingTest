# Approach 1: Array or List
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.value = []
        
    def next(self, val: int) -> float:
        if len(self.value) == self.size:
            del self.value[0]
        self.value.append(val)
        return sum(self.value) / len(self.value)
      
# Approach 2: Double-ended Queue
# First of all, one might notice that we do not need to keep all values from the data stream, 
# but rather the last n values which falls into the moving window.

# time complexity  - O(1)
# space complexity  - O(N) 

from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.size, self.count)
      
      
 # Approach 3: Circular Queue with Array
# No need to resort to any library, one could easily implement a circular queue with a fixed-size array. 
from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head+1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
        
