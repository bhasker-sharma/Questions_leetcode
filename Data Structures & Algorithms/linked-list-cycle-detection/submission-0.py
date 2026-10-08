# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        track =[]
        current = head
        while current is not None:
            if current in track:
                return True
            else:
                track.append(current)
                current = current.next
                
        return False 

        