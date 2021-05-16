class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = set()
        def dfs(node):
            # 노드가 없다면 반환 
            if not node :
                return None
            # current value delete 
            if node.val in to_delete:
                left = dfs(node.left)
                right = dfs(node.right)
                if left :
                    ans.add(left)
                if right:
                    ans.add(right)
            # not curerent 
            else :
                if len(ans) == 0 :
                    ans.add(node)
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
            
            
        dfs(root)
        return ans 
