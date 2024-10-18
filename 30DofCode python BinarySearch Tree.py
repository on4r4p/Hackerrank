

    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        left_ln = self.getHeight(root.left)
        right_ln = self.getHeight(root.right)
        return(max(left_ln,right_ln)+1)
         
        

