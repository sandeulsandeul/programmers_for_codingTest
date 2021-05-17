class SnapshotArray:

    def __init__(self, length: int):
      # i think this variable name is good 
      # cause cache is easy to know 
        self.cache = collections.defaultdict(list) # i think i have to use this function omg 
        self.id = 0

        # maybe .......
        # this data structure is 
        # [[[snapshot_id, val],[snapshot_id, val],[snapshot_id, val]] , [[snapshot_id, val],[snapshot_id, val],[snapshot_id, val]] 
    def set(self, index: int, val: int) -> None:
        if self.cache[index] and self.cache[index][-1][0]==self.id:
            self.cache[index][-1][-1] = val
        else:
            self.cache[index].append([self.id,val])

    def snap(self) -> int:
        val = self.id
        self.id+=1
        return val

    def get(self, index: int, snap_id: int) -> int:
        nums = self.cache[index
                          
        # this is for exceptional situation 
        # this part is too important  
        # when i take the test, i have to ask this part to interviewer          
        if not nums:
            return 0
         
        
        # binary search is useful algorithm !
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid][0] > snap_id:
                right = mid
            else:
                left = mid + 1
           
        if nums[left][0]<=snap_id:
            return nums[left][-1]
        
        if left-1>=0 :
            return nums[left-1][-1]
        
        return 0
##### bad code ####
# because this code needs too much time...bb
# time complexity is too heavy...omg

class SnapshotArray:
    import copy
    def __init__(self, length: int):
        self.array = [0]*length
        self.length = length
        self.snap_id = -1 
        self.snap_array = [ ]
        
    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        

    def snap(self) -> int:
        self.snap_id  += 1
        curr_array = copy.deepcopy(self.array)
        self.snap_array.append(curr_array)
        return self.snap_id 
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_array[snap_id][index]

