import unittest
from random import random, shuffle

from lib.linked_list import (
    SinglyLinkedList,
    SortedSinglyLinkedList,
    DoublyLinkedList,
    SortedDoublyLinkedList
)


class TestLinkedList(unittest.TestCase):

    def test_signly_linked_list(self):
        self.__test_insert(SinglyLinkedList)
        self.__test_search(SinglyLinkedList)
        self.__test_delete_for_one_node(SinglyLinkedList)
        self.__test_delete_for_last_node_for_unsorted(SinglyLinkedList)
        self.__test_delete_general(SinglyLinkedList)
        self.__test_minimum(SinglyLinkedList)
        self.__test_maximum(SinglyLinkedList)
        self.__test_predecessor_for_unsorted(SinglyLinkedList)
        self.__test_successor_for_unsorted(SinglyLinkedList)
        self.__test_is_empty(SinglyLinkedList)

    def test_sorted_signly_linked_list(self):
        self.__test_insert(SortedSinglyLinkedList)
        self.__test_search(SortedSinglyLinkedList)
        self.__test_delete_for_one_node(SortedSinglyLinkedList)
        self.__test_delete_for_last_node_for_sorted(SortedSinglyLinkedList)
        self.__test_delete_general(SortedSinglyLinkedList)
        self.__test_minimum(SortedSinglyLinkedList)
        self.__test_maximum(SortedSinglyLinkedList)
        self.__test_predecessor_for_sorted(SortedSinglyLinkedList)
        self.__test_successor_for_sorted(SortedSinglyLinkedList)
        self.__test_is_empty(SortedSinglyLinkedList)

    def test_doubly_linked_list(self):
        self.__test_insert(DoublyLinkedList)
        self.__test_search(DoublyLinkedList)
        self.__test_delete_for_one_node(DoublyLinkedList)
        self.__test_delete_for_last_node_for_unsorted(DoublyLinkedList)
        self.__test_delete_general(DoublyLinkedList)
        self.__test_minimum(DoublyLinkedList)
        self.__test_maximum(DoublyLinkedList)
        self.__test_predecessor_for_unsorted(DoublyLinkedList)
        self.__test_successor_for_unsorted(DoublyLinkedList)
        self.__test_is_empty(DoublyLinkedList)

    def test_sorted_doubly_linked_list(self):
        self.__test_insert(SortedDoublyLinkedList)
        self.__test_search(SortedDoublyLinkedList)
        self.__test_delete_for_one_node(SortedDoublyLinkedList)
        self.__test_delete_for_last_node_for_sorted(SortedDoublyLinkedList)
        self.__test_delete_general(SortedDoublyLinkedList)
        self.__test_minimum(SortedDoublyLinkedList)
        self.__test_maximum(SortedDoublyLinkedList)
        self.__test_predecessor_for_sorted(SortedDoublyLinkedList)
        self.__test_successor_for_sorted(SortedDoublyLinkedList)
        self.__test_is_empty(SortedDoublyLinkedList)

    def __test_insert(self, linked_list):
        for _ in range(0, 100):
            ll = linked_list()
            count = 0
            for _ in range(0, 100):
                count += 1
                r = random()
                node = ll.insert(r)
                self.assertEqual(node.var, r)
                self.assertEqual(len(ll), count)

    def __test_search(self, linked_list):
        # dependent methods: insert
        ll = linked_list()
        for _ in range(0, 100):
            r = random()
            ll.insert(r)
            self.assertIsNot(ll.search(r), None)

    def __test_delete_for_one_node(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        for _ in range(0, 100):
            r = random()
            node = ll.insert(r)
            self.assertIsNot(ll.search(r), None)
            try:
                ll.delete(node)
            except Exception:
                self.fail()

    def __test_delete_for_last_node_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        ns = []
        r = random()
        ll.insert(r)
        ns.append(r)
        self.assertIsNot(ll.search(r), None)
        for _ in range(0, 100):
            try:
                while len(ns) > 0 and random() > 0.5:
                    node = ll.search(ns[-1])
                    ll.delete(node)
                    del ns[-1]
            except Exception:
                self.fail()
            while True:
                r = random()
                ll.insert(r)
                ns.append(r)
                self.assertIsNot(ll.search(r), None)
                if random() > 0.5:
                    break
            

    def __test_delete_for_last_node_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        ns = []
        r = random()
        ll.insert(r)
        ns.append(r)
        self.assertIsNot(ll.search(r), None)
        for _ in range(0, 1000):
            try:
                while len(ns) > 0 and random() > 0.5:
                    node = ll.search(ns[-1])
                    ll.delete(node)
                    del ns[-1]
            except Exception:
                self.fail()
            while True:
                r += random()
                ll.insert(r)
                ns.append(r)
                self.assertIsNot(ll.search(r), None)
                if random() > 0.5:
                    break

    def __test_delete_general(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        ns = []
        for _ in range(0, 100):
            while True:
                r = random()
                ll.insert(r)
                ns.append(r)
                self.assertIsNot(ll.search(r), None)
                if random() > 0.5:
                    break
            while len(ns) > 0 and random() > 0.5:
                try:
                    rand_index = randint(0, len(ns) - 1)
                    node = ll.search(ns[rand_index])
                    ll.delete(node)
                    del ns[rand_index]
                except Exception:
                    self.fail()

    def __test_minimum(self, linked_list):
        # dependent methods: insert
        for _ in range(0, 100):
            ll = linked_list()
            sorted_ns = []
            r = random()
            for _ in range(0, 100):
                sorted_ns.append(r)
                r += random()
            random_ns = sorted_ns[:]
            shuffle(random_ns)
            for n in random_ns:
                ll.insert(n)
            self.assertEqual(ll.minimum().var, sorted_ns[0])

    def __test_maximum(self, linked_list):
        # dependent methods: insert
        for _ in range(0, 100):
            ll = linked_list()
            sorted_ns = []
            r = random()
            for _ in range(0, 100):
                sorted_ns.append(r)
                r += random()
            random_ns = sorted_ns[:]
            shuffle(random_ns)
            for n in random_ns:
                ll.insert(n)
            self.assertEqual(ll.maximum().var, sorted_ns[-1])

    def __test_predecessor_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        random_ns = [random() for _ in range(0, 300)]
        for n in random_ns:
            ll.insert(n)

        prev = ll.search(random_ns[0])
        self.assertIs(ll.predecessor(prev), None)
        for n in random_ns[1:]:
            curr = ll.search(n)
            self.assertEqual(ll.predecessor(curr), prev)
            prev = curr

    def __test_predecessor_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        sorted_ns = [n for n in range(0, 300)]
        random_ns = sorted_ns[:]
        shuffle(random_ns)
        for n in random_ns:
            ll.insert(n)

        self.assertIs(ll.predecessor(ll.search(sorted_ns[0])), None)
        for index in range(0, len(sorted_ns) - 1):
            prev = ll.search(sorted_ns[index])
            curr = ll.search(sorted_ns[index + 1])
            self.assertEqual(ll.predecessor(curr), prev)

    def __test_successor_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        random_ns = [random() for _ in range(0, 300)]
        for n in random_ns:
            ll.insert(n)

        next = ll.search(random_ns[-1])
        self.assertIs(ll.successor(next), None)
        for n in random_ns[::-1][1:]:
            curr = ll.search(n)
            self.assertEqual(ll.successor(curr), next)
            next = curr

    def __test_successor_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        sorted_ns = [n for n in range(0, 300)]
        random_ns = sorted_ns[:]
        shuffle(random_ns)
        for n in random_ns:
            ll.insert(n)

        self.assertIs(ll.successor(ll.search(sorted_ns[-1])), None)
        for index in range(0, len(sorted_ns) - 1):
            curr = ll.search(sorted_ns[index])
            next = ll.search(sorted_ns[index + 1])
            self.assertEqual(ll.successor(curr), next)

    def __test_is_empty(self, linked_list):
        # dependent methods: insert, search, delete
        ll = linked_list()
        ns = []
        for _ in range(0, 100):
            self.assertEqual(len(ns) == 0, ll.is_empty())
            if random() > 0.6:
                r = random()
                ll.insert(r)
                ns.append(r)
            if random() > 0.4 and len(ns) != 0:
                ll.delete(ll.search(ns[-1]))
                del ns[-1]
