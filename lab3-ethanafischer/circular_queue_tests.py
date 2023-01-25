import unittest

from circular_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size, CircularQueue)


class Tests(unittest.TestCase):
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    def test_is_empty_2(self):
        q = CircularQueue()
        q.items = [10, 20, 30, 40, 50, 60]
        q.start = 0
        q.capacity = 6
        q.size = 6
        self.assertFalse(is_empty(q))

    def test_enqueue(self):
        q = CircularQueue()
        q.items = [10, 20, 30, 40, 50, 60]
        q.start = 0
        q.capacity = 6
        q.size = 6
        my_q = [10, 20, 30, 40, 50, 60, 70, None, None, None, None, None]

        enqueue(q, 70)
        self.assertEqual(q.items, my_q)
        self.assertEqual(peek(q), my_q[0])
        self.assertEqual(q.size, 7)

    def test_enqueue_2(self):
        q2 = CircularQueue()
        q2.items = [None, None, 30, 40, 50, 60]
        q2.start = 2
        q2.capacity = 6
        q2.size = 4
        my_q = [10, None, 30, 40, 50, 60]

        enqueue(q2, 10)
        self.assertEqual(q2.items, my_q)
        self.assertEqual(q2.size, 5)

    def test_dequeue(self):
        q = CircularQueue()
        q.items = [10, 20, 30, 40, 50, 60]
        q.start = 0
        q.capacity = 6
        q.size = 6
        my_q = [None, 20, 30, 40, 50, 60]

        dequeue(q)
        self.assertEqual(q.items, my_q)
        self.assertEqual(q.size, 5)
        self.assertEqual(q.start, 1)

    def test_dequeue_2(self):
        q2 = CircularQueue()
        q2.items = [None, None, 30, 40, 50, 60]
        q2.start = 2
        q2.capacity = 6
        q2.size = 4
        my_q = [None, None, None, 40, 50, 60]

        dequeue(q2)
        self.assertEqual(q2.items, my_q)
        self.assertEqual(q2.size, 3)
        self.assertEqual(q2.start, 3)

    def test_dequeue_IndexError(self):
        q = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(q)

    def test_peek(self):
        q = CircularQueue()
        q.items = [10, 20, 30, 40, 50, 60]
        q.start = 0
        q.capacity = 6
        q.size = 6
        self.assertEqual(peek(q), 10)

    def test_peek_IndexError(self):
        q = empty_queue()
        with self.assertRaises(IndexError):
            peek(q)

    def test_size(self):
        q = CircularQueue()
        q.items = [10, 20, 30, 40, 50, 60]
        q.start = 0
        q.capacity = 6
        q.size = 6
        self.assertEqual(size(q), q.size)


if __name__ == '__main__':
    unittest.main()
