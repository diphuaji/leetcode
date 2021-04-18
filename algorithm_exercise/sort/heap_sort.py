import random


def has_parent(i, root):
    return i > root


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def has_left(i, heap_size):
    return left(i) < heap_size


def has_right(i, heap_size):
    return right(i) < heap_size


def swap(the_list, pos_old, pos_new):
    tmp = the_list[pos_old]
    the_list[pos_old] = the_list[pos_new]
    the_list[pos_new] = tmp


def build_heap(the_list):
    heap_size = len(the_list)

    root = 0
    while root < heap_size:
        pos = heap_size - 1
        while has_parent(pos, root):
            p = parent(pos)
            if has_left(p, heap_size):
                pos_to_swap = left(p)
                if has_right(p, heap_size) and the_list[right(p)] > the_list[left(p)]:
                    pos_to_swap = right(p)
                if the_list[pos_to_swap] > the_list[p]:
                    swap(the_list, p, pos_to_swap)
            pos -= 2
        root += 1


def sift_down(the_list, heap_size):
    pos = 0
    should_continue = True
    while should_continue:
        should_continue = False
        if has_left(pos, heap_size):
            pos_to_swap = left(pos)
            if has_right(pos, heap_size) and the_list[right(pos)] > the_list[left(pos)]:
                pos_to_swap = right(pos)

            if the_list[pos_to_swap] > the_list[pos]:
                swap(the_list, pos, pos_to_swap)
                pos = pos_to_swap
                should_continue = True


def heap_sort(the_list):
    build_heap(the_list)
    heap_size = len(the_list)
    while heap_size > 1:
        swap(the_list, 0, heap_size - 1)

        heap_size -= 1
        sift_down(the_list, heap_size)


a_list = [random.randint(-10000, 10000) for x in xrange(1000)]
heap_sort(a_list)
print a_list
