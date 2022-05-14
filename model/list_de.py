from .node import Node
from .ship_distribution import ShipDistribution

class ListDe:
    def __init__(self, data):
        self.head = None
        self.count = 0

    def add(self, data:ShipDistribution):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
            temp.next.previous = temp
        self.count =+ 1

    def add_to_start(self, data:ShipDistribution):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.count =+ 1

    def list(self):
        list = []
        if self.head != None:
            temp = self.head
            while temp.next != None:
                list.append(temp.data)
                temp = temp.next
        return list

