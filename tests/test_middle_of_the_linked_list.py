from middle_of_the_linked_list import LinkedList
import pytest


@pytest.mark.parametrize("input_date,expected_result", [
    ([1, 2, 3], 2),
    ([1, 2, 4, 3], 4),
    ([1], 1)
])
def test_middle_of_the_linked_list(input_date, expected_result):
    llist = LinkedList()

    for elem in input_date:
        llist.append(elem)

    assert llist.middle_node().data == expected_result
