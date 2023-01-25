import unittest

from heap import (
    MaxHeap, enqueue, dequeue, peek, size, _contents, heapify, heap_sort)


class Tests(unittest.TestCase):
    def test_heap_simple_operations(self):
        my_heap = MaxHeap()
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

        enqueue(my_heap, 10)

        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [10])
        self.assertEqual(peek(my_heap), 10)

        self.assertEqual(dequeue(my_heap), 10)

        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

    def test_heap_simple_operations_02(self):
        my_heap = MaxHeap()
        enqueue(my_heap, 0)
        enqueue(my_heap, 26)
        enqueue(my_heap, -23)
        enqueue(my_heap, 6)
        enqueue(my_heap, 1)

        self.assertEqual(size(my_heap), 5)
        self.assertEqual(_contents(my_heap), [26, 6, -23, 0, 1])
        self.assertEqual(peek(my_heap), 26)

        self.assertEqual(dequeue(my_heap), 26)
        self.assertEqual(dequeue(my_heap), 6)
        self.assertEqual(dequeue(my_heap), 1)
        self.assertEqual(dequeue(my_heap), 0)
        self.assertEqual(dequeue(my_heap), -23)

        with self.assertRaises(IndexError):
            dequeue(my_heap)

        with self.assertRaises(IndexError):
            peek(my_heap)

    def test_heapify_simple(self):
        my_heap = heapify([10, 20])
        self.assertEqual(size(my_heap), 2)
        self.assertEqual(_contents(my_heap), [20, 10])

    def test_heapify_simple_02(self):
        my_heap = heapify([34, 3, 24, 1, -12, 2, 5, 12, 0, 25, 240, 1616006, -251])
        self.assertEqual(_contents(my_heap), [1616006, 240, 34, 12, 25, 24, 5, 1, 0, 3, -12, 2, -251])

    def test_heapify_simple_03(self):
        my_heap = heapify([])
        self.assertEqual(_contents(my_heap), [])

    def test_heap_sort_simple(self):
        my_list = [20, 10]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20])

    def test_heap_sort_simple_02(self):
        my_list = [34, 3, 24, 1, -12, 2, 5, 12, 0, 25, 240, 1616006, -251]
        heap_sort(my_list)

        self.assertEqual(my_list, [-251, -12, 0, 1, 2, 3, 5, 12, 24, 25, 34, 240, 1616006])

    def test_heap_sort_simple_03(self):
        my_list = []
        heap_sort(my_list)

        self.assertEqual(my_list, [])

    def test_heap_sort_simple_04(self):
        my_list = [90, 89, 70, 36, 75, 63, 65, 21, 18, 15]
        heap_sort(my_list)

        self.assertEqual(my_list, [15, 18, 21, 36, 63, 65, 70, 75, 89, 90])

if __name__ == '__main__':
    unittest.main()
