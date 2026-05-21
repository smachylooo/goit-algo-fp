from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional

@dataclass
class Node:
    data: int
    next: Optional["Node"] = None

class LinkedList:
    def __init__(self, values: Iterable[int] | None = None) -> None:
        self.head: Optional[Node] = None
        if values:
            for value in values:
                self.append(value)

    def append(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self) -> None:
        print(" -> ".join(map(str, self.to_list())) or "Empty list")

def reverse_list(head: Optional[Node]) -> Optional[Node]:
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

def get_middle(head: Node) -> Node:
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    return slow


def merge_sorted_lists(left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
    dummy = Node(0)
    tail = dummy

    while left is not None and right is not None:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left is not None else right
    return dummy.next

def merge_sort(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    right_head = middle.next
    middle.next = None
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_head)

    return merge_sorted_lists(left_sorted, right_sorted)

if __name__ == "__main__":
    linked_list = LinkedList([7, 3, 9, 1, 5, 2])
    print("Original list:")
    linked_list.print_list()
    linked_list.head = reverse_list(linked_list.head)
    print("\nReversed list:")
    linked_list.print_list()
    linked_list.head = merge_sort(linked_list.head)
    print("\nSorted list:")
    linked_list.print_list()
    list_a = LinkedList([1, 4, 6])
    list_b = LinkedList([2, 3, 5, 8])
    merged = LinkedList()
    merged.head = merge_sorted_lists(list_a.head, list_b.head)
    print("\nMerged sorted lists:")
    merged.print_list()
