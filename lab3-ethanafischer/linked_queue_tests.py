import unittest

from linked_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size, LinkedQueue, Node)


class Tests(unittest.TestCase):
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    def test_is_empty_2(self):
        my_queue = LinkedQueue()
        enqueue(my_queue, 10)
        self.assertFalse(is_empty(my_queue))

    def test_enqueue(self):
        my_queue = LinkedQueue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(my_queue.head.next.value, 20)
        self.assertEqual(my_queue.head.value, 10)
        self.assertEqual(my_queue.size, 3)

    def test_dequeue(self):
        my_queue = LinkedQueue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        dequeue(my_queue)
        dequeue(my_queue)
        self.assertEqual(my_queue.head.value, 30)
        self.assertEqual(my_queue.size, 1)

    def test_dequeue_IndexError(self):
        my_queue = LinkedQueue()
        with self.assertRaises(IndexError):
            dequeue(my_queue)

    def test_peek(self):
        my_queue = LinkedQueue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(peek(my_queue), my_queue.head.value)

    def test_peek_IndexError(self):
        my_queue = LinkedQueue()
        with self.assertRaises(IndexError):
            peek(my_queue)

    def test_size(self):
        my_queue = LinkedQueue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(size(my_queue), my_queue.size)


if __name__ == '__main__':
    unittest.main()
