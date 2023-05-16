import pytest
from super_linked_list import Node, SuperLinkedList

def test_exists():
    assert SuperLinkedList

# @pytest.mark.skip("TODO")
def test_print():
    ll = SuperLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    actual = ll.__str__()
    expected = "['1', '2', '3']"
    assert actual == expected

def test_traverse():
    ll = SuperLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    output_list = list()
    for item in ll:
        output_list.append(item)
    actual = output_list
    expected = [1, 2, 3]
    assert actual == expected

def test_count():
    ll = SuperLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    output_list = list()
    actual = len(ll)
    expected = 3
    assert actual == expected