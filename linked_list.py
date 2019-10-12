'''
Linked lists are an alternative for arrays
each linked list consists of nodes, each node has 2 elements
data it contains and 'next' a pointer to the next element in the list
'''

class Node:
    '''A single node, part of linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''entire list, consist of Node objects'''
    def __init__(self):
        self.head = None

    def print_list(self):
        '''print all data in the list'''
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        print("Head node data: ", self.head.data)

    def append(self, data):
        '''appending data to the end of the list'''
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        #keep iterating until the last node isnt null, whitch means we've reached the end of it
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        '''appending data to the begging of the list'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        '''Inserts data after given node'''
        if not prev_node:
            print('Previous node is not in a list')
            return
      
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        '''deletes a node by given key

        key -> data of node to be deleted'''

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node.data = None
            return
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node.data = None

    def delete_node_at_pos(self, pos):
        '''deletes node at given position (starting from 0)
        pos -> position of node to be deleted'''

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node.data = None
            return

        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def reverse_iterative(self):
        '''reverses the list iterative way
        ex:
        A -> B -> C -> D
        D -> C -> B -> A'''

        prev_node = None
        cur_node = self.head
        while cur_node:
            #store the pointer to keep track of the next node after changing the .next property
            next_pointer = cur_node.next

            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_pointer
        
        #reset the head after reversing
        self.head = prev_node

    def reverse_recursive(self):
        '''reverses the list recursive way
        ex:
        A -> B -> C -> D
        D -> C -> B -> A'''

        def _reverse_recursive(cur_node, prev_node):
            if not cur_node:
                return prev_node
         
            #store the pointer to keep track of the next node after changing the .next property
            next_pointer = cur_node.next

            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_pointer
            return _reverse_recursive(cur_node, prev_node)

        self.head = _reverse_recursive(cur_node=self.head, prev_node=None)

    def swap(self, key_1, key_2):
        '''swaps two nodes by given key (data) values
        key_1, key_2 => data of nodes to swap'''
        
        if key_1 == key_2:
            return

        prev_1 = None       
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None       
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return print("List index out of range")

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


    def swap_at_pos(self, pos1, pos2):
        '''swaps data of two nodes by given position
        pos1, pos2 => positions of data to be swapped'''

        if pos1 == pos2:
            return

        cur_node = self.head
        
        count = 0
        while cur_node and count <= pos1:
            if count == pos1:
                data1 = cur_node.data
                node1 = cur_node
                cur_node = self.head
            else:
                cur_node = cur_node.next
            count += 1
        
        count = 0
        while cur_node and count <= pos2:
            if count == pos2:
                node1.data = cur_node.data
                cur_node.data = data1
            else:
                cur_node = cur_node.next
            count += 1
        
        if not cur_node:
            print("List index out of range")


    def rotate(self, pos):
        '''rotates the list at given position
        ex.
        A -> B -> C -> D -> E
        after rotating at pos = 2:
        D -> E -> A -> B -> C'''
        cur_node, last_node = self.head, self.head

        count = 0
        while cur_node and pos > count:
            cur_node = cur_node.next
            last_node = last_node.next
            count += 1
        print("cur: ", cur_node.data)

        prev_node = None
        while last_node:
            prev_node = last_node
            last_node = last_node.next
        last_node = prev_node
        print("last: ", last_node.data)

        last_node.next = self.head
        self.head = cur_node.next
        cur_node.next = None

    def merge_sorted(self, llist):
        '''merges two lists with SORTED data
        llist -> linked list instance to merge'''
        pointer_1 = self.head
        pointer_2 = llist.head
        lower_val = None

        if not pointer_1:
            return pointer_2
        if not pointer_2:
            return pointer_1

        if pointer_1 and pointer_2:
            if pointer_1.data <= pointer_2.data:
                lower_val = pointer_1
                pointer_1 = lower_val.next
            else:
                lower_val = pointer_2
                pointer_2 = lower_val.next

            new_head = lower_val

        while pointer_1 and pointer_2:
            if pointer_1.data <= pointer_2.data:
                lower_val.next = pointer_1
                lower_val = pointer_1
                pointer_1 = lower_val.next
            else:
                lower_val.next = pointer_2
                lower_val = pointer_2
                pointer_2 = lower_val.next
        if not pointer_1:
            lower_val.next = pointer_2
        if not pointer_2:
            lower_val.next = pointer_1
      
        return new_head

    def length(self):
        '''Returns the length of linked list'''

        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def remove_duplicates(self):
        '''Deletes all the duplicate nodes in the linked list.'''

        cur_node = self.head
        dup_vals = dict()

        while cur_node:
            if cur_node.data in dup_vals:
                self.delete_node(cur_node.data)
            else:
                dup_vals[cur_node.data] = 1

            cur_node = cur_node.next
           

    def pos(self, pos):
        '''Return node at given position'''
        cur_node = self.head
        count = 0
        while cur_node and pos > count:

            cur_node = cur_node.next
            count += 1

        return cur_node

    def sum_two_lists(self, llist):
        '''Sums up two llist of digits as if they were a number.
        The numbers need to be appended from the highest ex. houndreds all the
        way to the number of units.
        So to sum up 315 + 29:
        llist_1.append(5)
        llist_1.append(1)
        llist_1.append(3)

        llist_2.append(9)
        llist_2.append(2)
        And then:
        llist_1.sum_of_two_lists(llist_2).

        Returns a linked list instance'''
        pointer_1 = self.head
        pointer_2 = llist.head

        sum_list = LinkedList()

        #adding numbers primary school way
        carry = 0
        while pointer_1 or pointer_2:
            if not pointer_1:
                digit_1 = 0
            else:
                digit_1 = pointer_1.data
        
            if not pointer_2:
                digit_2 = 0
            else:
                digit_2 = pointer_2.data

            sum_of_digits = digit_1 + digit_2 + carry

            if sum_of_digits >= 10:
                sum_of_digits %= 10
                carry = 1
            else:
                carry = 0

            sum_list.append(sum_of_digits)

            if pointer_1:
                pointer_1 = pointer_1.next
            
            if pointer_2:
                pointer_2 = pointer_2.next

        return sum_list
     


def main():
    '''main'''
    llist = LinkedList()
    llist_2 = LinkedList()
    # llist.append("A")
    # llist.append("B")
    # llist.append("C")
    # llist.append("D")
    # llist.append("E")
    # llist.delete_node("B")
    # llist.delete_node_at_pos(2)
    # llist.insert_after_node(llist.head.next, "E")

    # llist.print_list()
    # print("Reversed")
    # llist.reverse_iterative()
    # llist.print_list()
    # print("Reversed Again")
    # llist.reverse_recursive()
    #llist.swap(1, 2)
    #llist.swap('C', 'A')
    # llist.print_list()
    # llist.rotate(2)
    llist.append(5)
    llist.append(6)
    llist.append(3)
    llist_2.append(8)
    llist_2.append(4)
    
    print(365 + 48)
    llist.sum_two_lists(llist_2).print_list()

if __name__ == '__main__':
    main()
