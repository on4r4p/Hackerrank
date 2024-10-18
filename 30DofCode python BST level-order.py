

    def levelOrder(self,root):
        #Write your code here
        levels = [root]
        order = []
        
        while levels:
            current = levels.pop(0)
            order.append(str(current.data))
            if current.left:levels.append(current.left)
            if current.right:levels.append(current.right)
        print(" ".join(order))

                
        

