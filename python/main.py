from typing import Any, TypeVar

TNode = TypeVar("TNode", bound="Node")


class Node:
    next: TNode | None

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    _initial: Node | None
    _size: int

    def __init__(self):
        self._initial = None
        self._size = 0

    def add(self, value: Any):
        new_node = Node(value)
        if self._size == 0:
            self._initial = new_node
        else:
            last_node: Node = self._initial
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, key):
        _key = key
        if key < 0:
            _key = self._size + key
        if _key < 0 or _key >= self._size:
            raise IndexError()
        node = self._initial
        for _ in range(_key):
            node = node.next
        return node.value

    def __setitem__(self, key, value):
        _key = key
        if key < 0:
            _key = self._size + key
        if _key < 0 or _key >= self._size:
            raise IndexError()
        node = self._initial
        for _ in range(_key):
            node = node.next
        node.value = value


if __name__ == "__main__":
    linkedlist = LinkedList()

    linkedlist.add(0)
    linkedlist.add(1)
    linkedlist.add(2)

    assert linkedlist._initial.value == 0
    assert linkedlist._initial.next.value == 1
    assert linkedlist._initial.next.next.value == 2

    assert linkedlist._size == 3
    assert len(linkedlist) == 3

    assert linkedlist[0] == 0
    assert linkedlist[1] == 1
    assert linkedlist[2] == 2

    assert linkedlist[-1] == 2
    assert linkedlist[-2] == 1
    assert linkedlist[-3] == 0

    try:
        linkedlist[3]
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    try:
        linkedlist[-4]
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    linkedlist[0] = 10
    linkedlist[1] = 11
    linkedlist[2] = 12

    assert linkedlist[0] == 10
    assert linkedlist[1] == 11
    assert linkedlist[2] == 12

    linkedlist[-1] = 13
    linkedlist[-2] = 14
    linkedlist[-3] = 15

    assert linkedlist[2] == 13
    assert linkedlist[1] == 14
    assert linkedlist[0] == 15

    try:
        linkedlist[-4] = 1
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    try:
        linkedlist[3] = 1
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)
