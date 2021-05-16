# Approach 1: Queue + Set

from collections import deque

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
          
# Approach 2: Hashtable / Dictionary
# Complexity Analysis
# Time Complexity: O(1). The lookup and update of the hashtable takes a constant time.
# Space Complexity: O(M) where M is the size of all incoming messages. Over the time, the hashtable would have an entry for each unique message that has appeared.

class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = { }
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timestamp :
            if self.timestamp[message] + 10 <= timestamp :
                self.timestamp[message] = timestamp
            else :
                return False
        else :
            self.timestamp[message] = timestamp
        return True 
