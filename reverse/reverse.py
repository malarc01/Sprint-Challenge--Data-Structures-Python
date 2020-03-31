class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

    def __repr__(self):
        return f'[Node-value={self.value}, next_node={self.next_node}]'


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        # print('B-self.head', self.head)
        node = Node(value)
        if self.head is not None:
            # print('NODE.VALUE', node.value)
            # print('b-node.next_node =>', node.next_node)

            # print('b-self.head.value =>', self.head.value)

            node.set_next(self.head)
            # print('a-self.head.value =>', self.head.value)
            # print('a-self.head.value =>', self.head.value)

            # print('a=node.value =>', node.value)
            # print('a=node.next_node =>', node.next_node)
            # print('a=node.next_node =>', node.next_node)
            # print('a=node.next_node.next_node', node.next_node.next_node)
            # print('a=node.next_node.next_node', node.next_node.next_node)
        # print('C-self.head=>', self.head)
        self.head = node
        # print('A-self.head==>', self.head)

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        # print('before-current')

        current = self.head
        # print('after-current')
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                # print('inside if loop for get value ')
                # print('current.value', current.value)
                return True
            # update our current node to the current node's next node
            # print('b-current', current)
            current = current.get_next()
            # print('a-current', current)
        # if we've gotten here, then the target node isn't in our list

        return False

    def reverse_list(self):
        prev = None
        current = self.head

        next = None

        print('current =>', current)

        while current is not None:
            # print(' b-next =>', next)
            next = current.next_node
            # print(' next =>', next)
            # print(' current =>', current)
            current.next_node = prev
            # print(' current.next_node =>', current.next_node)

            # print(' b-prev =>', prev)
            # print(' b-current =>', current)

            prev = current
            # print(' a-prev =>', prev)
            # print(' a-current =>', current)

            # print(' b-current =>', current)
            # print(' b-next =>', next)

            current = next
            # print(' a-current =>', current)
            # print(' a-next =>', next)

            # return 'Ran Once'
        self.head = prev
        # return 'done'


#
linked_list = LinkedList()

# add_to_head(item)
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
linked_list.add_to_head(5)
# print(linked_list.head.value)
# print(linked_list.reverse_list())
# print(linked_list.head.value)


# contains(item)
# print(linked_list.contains(2))


# at the head of linked list
# linked_list.contains(10)

# in the middle of 3 nodes
# print(linked_list.contains(1000))


# print(linked_list.contains(10))
# print(linked_list.contains(1000))

# linked_list.add_to_head(77)
# print("PRINT linked_list.head.value =>", linked_list.head.value)

# print("PRINT linked_list.head.value =>", linked_list.head.value)

# print("PRINT linked_list.head.next_node.value =>", linked_list.head.next_node)
# print("PRINT linked_list.head.next_node.value =>",
# linked_list.head.next_node.next_node)
# print("PRINT linked_list.head.next_node.value =>",
# linked_list.head.next_node.value)
