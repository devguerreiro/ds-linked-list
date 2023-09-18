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

    def _get_node(self, index: int):
        _index = index
        if index < 0:
            _index = self._size + index
            if _index < 0:
                raise IndexError()
        node = self._initial
        for _ in range(_index):
            if node is None:
                raise IndexError()
            node = node.next
        return node

    def __getitem__(self, key):
        if self._size == 0:
            raise IndexError()
        node = self._get_node(key)
        return node.value

    def __setitem__(self, key, value):
        node = self._get_node(key)
        node.value = value

    def index(self, value):
        index = 0
        node = self._initial
        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return -1

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self._initial
            self._initial = new_node
        else:
            previous_node = self._get_node(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
        self._size += 1


if __name__ == "__main__":
    linkedlist = LinkedList()

    BIG_INDEX = 2**100

    linkedlist.add(10)
    linkedlist.add(11)
    linkedlist.add(12)

    # check length
    assert linkedlist._size == 3
    assert len(linkedlist) == 3

    # check getitem
    assert linkedlist[0] == 10
    assert linkedlist[1] == 11
    assert linkedlist[2] == 12

    # check inverted getitem
    assert linkedlist[-1] == 12
    assert linkedlist[-2] == 11
    assert linkedlist[-3] == 10

    # check index
    assert linkedlist.index(10) == 0
    assert linkedlist.index(11) == 1
    assert linkedlist.index(12) == 2

    # check index of inexistent
    assert linkedlist.index(BIG_INDEX) == -1

    # check getitem of an index bigger than length
    try:
        linkedlist[BIG_INDEX]
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    # check getitem of an index smaller than negative length
    try:
        linkedlist[-BIG_INDEX]
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    # check setitem
    linkedlist[0] = 20
    linkedlist[1] = 21
    linkedlist[2] = 22

    assert linkedlist[0] == 20
    assert linkedlist[1] == 21
    assert linkedlist[2] == 22

    # check inverted setitem
    linkedlist[-1] = 32
    linkedlist[-2] = 31
    linkedlist[-3] = 30

    assert linkedlist[2] == 32
    assert linkedlist[1] == 31
    assert linkedlist[0] == 30

    # check getitem of an index bigger than length
    try:
        linkedlist[BIG_INDEX] = 1
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    # check setitem of an index smaller than negative length
    try:
        linkedlist[-BIG_INDEX] = 1
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    # check insert before initial
    aux = linkedlist[0]
    linkedlist.insert(0, 150)
    assert linkedlist[0] == 150
    assert linkedlist[1] == aux

    # check insert in the middle
    aux = linkedlist[2]
    linkedlist.insert(2, 232)
    assert linkedlist[2] == 232
    assert linkedlist[3] == aux

    # check insert after last
    aux = linkedlist[len(linkedlist) - 1]
    linkedlist.insert(len(linkedlist), 345)
    assert linkedlist[len(linkedlist) - 1] == 345
    assert linkedlist[len(linkedlist) - 2] == aux
