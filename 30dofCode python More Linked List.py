

    def removeDuplicates(self,head):
        tmp = {head.data}
        newhead = Node(head.data)
        current = head.next
        current_new = newhead
        while current:
            if current.data not in tmp:
                 tmp.add(current.data)
                 current_new.next = Node(current.data)
                 current_new = current_new.next
            current = current.next
        return newhead

