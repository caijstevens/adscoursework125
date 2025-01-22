


def show(linked_list):
    current_element = linked_list.head
    while current_element != None:
        print(str(current_element.data))
        current_element = current_element.next
    print("NULL")



def cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists.

    Returns a LinkedList which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    current_check = linked_list_a.head
    while current_check.next != None:
        current_check = current_check.next
    current_check.next = linked_list_b.head
    return linked_list_a

def smart_cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists, both with tail references.

    Returns a LinkedListWithTail which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    if linked_list_a.head == None:
        linked_list_a.head = linked_list_b.head
        linked_list_a.tail = linked_list_b.tail
        return linked_list_a
    if linked_list_b.head != None:
        linked_list_a.tail.next = linked_list_b.head
        linked_list_a.tail = linked_list_b.tail
        return linked_list_a


def make_queue():
    """Creates a linked list with the required structure.

    Returns a LinkedListWithTail containing the contents of Q as described in the 
    question.
    """
    queueQ = [4, 9, 18, 3, 21]
    ll_Q = LinkedListWithTail()
    for i in range(0, len(queueQ)):
        next_node = Node(queueQ[i])
        if ll_Q.head == None:
            ll_Q.head = next_node
            ll_Q.tail = next_node
        else:
            ll_Q.tail.next = next_node
            ll_Q.tail = next_node
    ll_Q.size = len(queueQ)
    return ll_Q



def enqueue(ll_queue, value):
    """Returns a linked list representing a queue, after a new value has been
    enqueued.

    Returns a LinkedListWithTail containing the contents of a queue held in the
    LinkedListWithTail ll_queue, after a new value has been enqueued.
    """
    extra_node = Node(value)
    ll_queue.tail.next = extra_node
    ll_queue.tail = extra_node
    ll_queue.size = ll_queue.size + 1
    return ll_queue

def convert_to_array_queue(ll_queue):
    """
    "Converts" a LinkedList to an array-backed queue.

    Given a LinkedList ll_queue containing a tuple (A, f, r) where: 

    A is a list of length 10, backing the queue
    f is an int with a value facilitating access to the front of the queue
    r is an int with a value facilitating access to the rear of the queue.
    """


