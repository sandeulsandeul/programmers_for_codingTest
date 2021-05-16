class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p , q , curr = l1 ,l2 , dummyHead
        carry = 0 
        while p or q :
            x = p.val if p else 0
            y = q.val if q else 0 
            sum_val = carry + x + y
            carry = ( sum_val ) // 10 
            curr.next = ListNode( sum_val % 10 )
            curr  = curr.next
            p = p.next if p else None
            q = q.next if q else None
        if carry > 0 :
            curr.next = ListNode( carry )
        return dummyHead.next
