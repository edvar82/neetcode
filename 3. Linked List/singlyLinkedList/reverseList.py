def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next  # Salva o próximo nó
        curr.next = prev       # Inverte a ligação
        prev = curr            # Avança prev
        curr = next_temp       # Avança curr
    
    # Ao final, prev será o novo head
    return prev