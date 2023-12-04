# initialize the Linked List Data-Structure with CRUD operations on it
class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Node is inserted at the beginning")
        else:
            new_node.next = self.head
            self.head = new_node
            print("Node is inserted at the beginning")

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_begin(data)
            print("Node is inserted at the given index")
        else:
            position = 0
            current_node = self.head
            while current_node and position + 1 < index:
                current_node = current_node.next
                position += 1
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
                print("Node is inserted at the given index")
            else:
                print("Invalid Index")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Node is inserted at the End")
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            print("Node is inserted at the End")

    def print_linked_list(self):
        temp = self.head
        list = []
        while temp:
            list.append(temp.data)
            temp = temp.next
        print("Linked list is")
        print(list)

    def update_node(self, value, index):
        current_node = self.head
        if index == 0:
            current_node.data = value
            print(f"Node is updated at the index {index}")
        else:
            while current_node != None and index > 0:
                current_node = current_node.next
                index -= 1
            if current_node != None:
                current_node.data = value
                print(f"Node is updated at the index {index}")
            else:
                print("Index is not present in linkedList")

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        print("Node at the beginning is removed")

    def remove_last_node(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        print("Node at the end is removed")

    def remove_at_index(self, index):
        if self.head == None:
            print("LinkedList is empty")
            return
        current_node = self.head
        if index == 0:
            self.remove_first_node()
            return
        while current_node != None and index - 1 > 0:
            current_node = current_node.next
            index -= 1
        if current_node != None:
            current_node.next = current_node.next.next
            print(f"Node at the give index {index} is removed")
        else:
            print("Index is not present in Linked List")

    def remove_node(self, data):
        if self.head == None:
            print("LinkedList is empty")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            print("Node with given data is removed from the Linked List")
            return
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next == None:
            print("Node with give data is not present in the LinkedList")
        else:
            current_node.next = current_node.next.next
            print("Node with given data is removed from the Linked List")

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest


ex_ll = LinkedList()
ex_ll.insert_at_begin(7)
ex_ll.insert_at_begin(8)
ex_ll.insert_at_index(1, 6)
ex_ll.insert_at_index(0, 5)
ex_ll.insert_at_index(1, 4)
ex_ll.insert_at_end(78)
ex_ll.insert_at_begin(1)
ex_ll.insert_at_begin(2)
ex_ll.remove_at_index(5)
ex_ll.remove_node(67)
ex_ll.print_linked_list()
ex_ll.head = ex_ll.reverse(ex_ll.head)
print("Reversed linked list is ")
ex_ll.print_linked_list()

# For a given count, using recursion return an array of fibonacci series with size matching the count
# 	Test-cases
# 	Input: 1
# 	Output: [1]
# —---------------------------
# 	Input: 5
# 	Output: [1, 1, 2, 3, 5]
# 		0 < n < 1000 (where n is the given count)


def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fibonacci_list = fibonacci_series(n - 1)
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        return fibonacci_list


print(
    "fibonacci series is",
)
print(fibonacci_series(1))
print(fibonacci_series(5))


# Reverse a LinkedList using recursion
# 	Test-cases
# 	Input: 1->2->3->4
# 	Output: 4->3->2->1
# —---------------------------
# 	Input: 1
# 	Output:

# 		0 < n < 1000 (where n is the number of elements in linked list)


# General Python
# Transpose a matrix using list comprehensions
# Use the above functions in list comprehension
def transpose_matrix(matrix):
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed_matrix


matrix = [[1, 2], [3, 4], [5, 6]]
transpose = transpose_matrix(matrix)
print(f"transpose of the matrix is {transpose}")


# create custom range function - custom_range using iter and next, without using loops
# should support the following cases
# custom_range(5) -> [0,5)
# custom_range(1,5) -> [1,5)
# custom_range(0, 6, 2) -> [0,2, 4]
# custom_range(6, 0, -2) -> [6, 4, 2]
# for i in custom_range(5)
# 	print(i) # 0,1,2,3,4


class custom_range_class:
    def __init__(self, *args):
        num_of_args = len(args)
        if num_of_args == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif num_of_args == 2:
            self.start, self.stop = args
            self.step = 1
        elif num_of_args == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(
                f"Expected atmost 3 args, got no of arguments {num_of_args}"
            )

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.start >= self.stop) or (
            self.step < 0 and self.start <= self.stop
        ):
            raise StopIteration
        current_val = self.start
        self.start += self.step
        return current_val


def custom_range(*args):
    custom_range_object = custom_range_class(*args)
    return custom_range_object


def custom_range_using_generator(*args):
    num_args = len(args)

    if num_args == 1:
        start, stop, step = 0, args[0], 1
    elif num_args == 2:
        start, stop, step = args[0], args[1], 1
    elif num_args == 3:
        start, stop, step = args
    else:
        raise TypeError(f"Expected at most 3 arguments, got {num_args}")

    while (step > 0 and start <= stop) or (step < 0 and start >= stop):
        yield start
        start += step


# create custom fibo function - custom_fibo using iter and next, without using loops
# should support the following cases
# custom_fibo(5) -> [1,1,2,3,5]
# for i in custom_fibo(5)
# 	print(i) # 1,1,2,3,5


class custom_fibonacci_series:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 1, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value


def custom_fibo(n):
    custom_fib_object = custom_fibonacci_series(n)
    return custom_fib_object


def custom_fib_using_generator(n):
    first = second = 1
    for i in range(n):
        yield first
        first, second = second, first + second


print("fibonacci series is")
fib_obj = custom_fib_using_generator(7)
for i in fib_obj:
    print(i)
