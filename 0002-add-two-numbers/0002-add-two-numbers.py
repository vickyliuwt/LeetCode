# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()          # 哨兵假节点
        cur = dummy                 # 一支"写字的笔"
        carry = 0                   # 进位
        while l1 or l2 or carry:    # 只要还有东西没处理完
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10     # 十位 → 进位
            digit = total % 10      # 个位 → 写下来
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next