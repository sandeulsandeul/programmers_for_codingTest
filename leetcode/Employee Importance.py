# 690. Employee Importance

# Runtime: 164 ms, faster than 26.31% of Python3 online submissions for Employee Importance.
# Memory Usage: 15.5 MB, less than 66.36% of Python3 online submissions for Employee Importance.
class MySolution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        subordinates_dic = []
        for employee in employees :
            if employee.id == id :
                subordinates = employee.subordinates
            dic[employee.id ] = ( employee.importance , employee.subordinates ) 
        ans = dic[id][0]
        def sumImportance (subordinate):
            tmp = dic[subordinate][0]
            for s in dic[subordinate][1]:
                tmp += sumImportance(s)
            return tmp
        for subordinate in subordinates :
            ans += sumImportance(subordinate)
        return ans
 # I think this solution is bad.. OMG
 # This is better 
 # Runtime: 156 ms, faster than 68.34% of Python3 online submissions for Employee Importance.
 # Memory Usage: 15.6 MB, less than 35.51% of Python3 online submissions for Employee Importance.

    def getImportance(self, employees: List['Employee'], query_id: int) -> int:
        emap = {e.id : e for e in employees} 
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance + sum ( dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)

