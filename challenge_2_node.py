import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.value >= value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)


def basic_check():
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)

    return contains(n2, 3)


def complex_check():
    n7 = Node(value=7, left=None, right=None)
    n15 = Node(value=15, left=None, right=None)
    n10 = Node(value=10, left=n7, right=n15)

    n20 = Node(value=20, left=None, right=None)
    n30 = Node(value=30, left=None, right=None)
    n25 = Node(value=25, left=n20, right=n30)

    n18 = Node(value=18, left=n10, right=n25)

    # Creating a root node
    root = Node(value=12, left=n10, right=n18)

    # Check if the tree contains a value
    all_nodes = [7, 15, 10, 20, 30, 25, 18, 12]
    for node in all_nodes:
        if not contains(root, node):
            return False
    if contains(root, 22):
        return False
    return True


if __name__ == '__main__':
    print(basic_check())
    print(complex_check())
