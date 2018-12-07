from linked_list import LinkedList

class Queue:
    def __init__ (self, items=None):
        self.linkedlist = LinkedList(items)

    def enqueue (self, item):
        self.linkedlist.append(item)

    def dequeue (self):
        self.linkedlist.delete(self.linkedlist.head.data)

    def items (self):
        return self.linkedlist.items()

def main ():
    queue = Queue(['1', '2', '3'])
    queue.enqueue('4')
    print(queue.items())
    queue.dequeue()
    print(queue.items())

if __name__ == '__main__':
    main()
