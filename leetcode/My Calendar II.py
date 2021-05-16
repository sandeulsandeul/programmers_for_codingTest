class MyCalendarTwo:
    
    def __init__(self):
        # just put in schedule in this list 
        self.calendar = []
        # when two schedule are conflicted, append in this list 
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        # checking overlaps , if some list conflict in overlaps list, this can not put in list 
        for i , j in self.overlaps:
            if start < j and end > i :
                return False
            
        # checking overlaps
        for i , j in self.calendar:
            if start < j and end > i :
                self.overlaps.append((max(start,i) , min(end,j )))
        self.calendar.append((start,end))
        return True 
        
     
