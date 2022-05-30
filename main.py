from doublelinkedlist import DoubleLinkedList
from random import randint


def main():
    a = DoubleLinkedList()
    for i in range(10):
        a.push_back(randint(0,100))
    print(a)
    a.sort(lambda a,b : b if a>b else a)
    print(a)
    for i in range(5):
        a.pop_front()
    
    for i in a:
        i *= 2
        
    print(a)

if __name__ == '__main__':
    main()
