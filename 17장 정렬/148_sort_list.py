# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge_sort(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid+1, right)

        left_idx = left
        right_idx = mid + 1
        temp = []

        while left_idx <= mid and right_idx <= right:
            if arr[left_idx] < arr[right_idx]:
                temp.append(arr[left_idx])
                left_idx += 1
            elif arr[left_idx] > arr[right_idx]:
                temp.append(arr[right_idx])
                right_idx += 1
            else:
                temp.append(arr[left_idx])
                temp.append(arr[right_idx])
                left_idx += 1
                right_idx += 1

        while left_idx <= mid:
            temp.append(arr[left_idx])
            left_idx += 1

        while right_idx <= right:
            temp.append(arr[right_idx])
            right_idx += 1

        idx = 0
        for i in range(left, right + 1):
            arr[i] = temp[idx]
            idx += 1
        return

    def sortList(self, head: ListNode) -> ListNode:
        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        self.merge_sort(arr, 0, len(arr)-1)

        node = head
        i = 0
        while node:
            node.val = arr[i]
            i += 1
            node = node.next

        return head

sol = Solution()
sol.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))


"""
Input
[4,2,1,3]
Output
[1,2,3,4]
"""
