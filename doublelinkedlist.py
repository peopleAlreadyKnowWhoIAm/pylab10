from typing import Any, Callable


class DoubleLinkedList:
    class Node:
        def __init__(self, previous_node = None, next_node = None, value: Any = None) -> None:
            self.previous_node = previous_node
            self.next_node = next_node
            self.value = value


    def __init__(self):
        self.__first = None
        self.__last = None
        self.__next = None

    def push_back(self, value: Any) -> None:
        if self.__last is None:
            self.__create_first_node(value)
        else:
            tmp = self.Node(self.__last, None, value)        
            self.__last.next_node = tmp
            self.__last = tmp

    def pop_back(self) -> None:
        if self.__last is None:
            raise AttributeError()
        if self.__last.previous_node is None:
            self.__first = None
            self.__last = None
        else:
            tmp = self.__last.previous_node
            tmp.next_node.previous_node = None
            tmp.next_node = None
            self.__last  = tmp
        

    def push_front(self, value: Any) -> None:
        if self.__first is None:
            self.__create_first_node(value)
        else:
            tmp = self.Node(None, self.__first, value)
            self.__first.previous_node = tmp
            self.__first = tmp

    def pop_front(self) -> None:
        if self.__first is None:
            raise AttributeError()
        if self.__first.next_node is None:
            self.__first = None
            self.__last = None
        else:
            tmp = self.__first.next_node
            tmp.previous_node.next_node = None
            tmp.previous_node = None
            self.__first = tmp

    def insert(self, element: Any, pos: int) -> None:
        before = self.__count(pos)
        to_paste = self.Node(before.previous_node, before, element)
        before.previous_node = to_paste
        if to_paste.previous_node is not None:
            to_paste.previous_node.next_node = to_paste
    
    def sort(self, key: Callable[[Any, Any], Any]) -> None:
        now = self.__first
        while now is not None:
            least_candidate = now.next_node
            least = now
            while least_candidate is not None:
                result = key(least_candidate.value, least.value)
                if result == least_candidate.value:
                    least = least_candidate
                least_candidate = least_candidate.next_node
            now.value, least.value = least.value, now.value
            now = now.next_node
                

    def __getitem__(self, a: int) -> Any:
        return self.__count(a).value

    def __create_first_node(self, value: Any) -> None:
        tmp = self.Node(None, None, value)
        self.__first = tmp
        self.__last = tmp
        
    def __count(self, index: int) -> Node:
        out = self.__first
        for _ in range(index):
            if out.next_node is None:
                raise OverflowError()
            out = out.next_node
        return out

    def __repr__(self) -> str:
        tmp = self.__first
        str_out = '['
        while tmp is not None:
            str_out += f' {tmp.value} ,' if tmp.next_node is not None else f' {tmp.value} '
            tmp = tmp.next_node
        str_out += ']'
        return str_out

    def __str__(self) -> str:
        return self.__repr__()

    def __iter__(self):
        if self.__first is None:
            raise StopIteration
        self.__next = self.__first
        return self

    def __next__(self):
        if self.__next is None:
            raise StopIteration()
        val = self.__next.value
        self.__next = self.__next.next_node
        return val

    def __del__(self):
        now = self.__first
        while now is not None:
            tmp = now
            now = now.next_node
            del tmp
