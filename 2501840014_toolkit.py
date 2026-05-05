# ---------------- BST IMPLEMENTATION ---------------- #

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end=" ")
            self._inorder(root.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)

        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self._min_value(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return root

    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# ---------------- GRAPH IMPLEMENTATION ---------------- #

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]

        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbour, _ in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbour, _ in self.graph.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)


# ---------------- MAIN FUNCTION ---------------- #

if __name__ == "__main__":

    print("===== BINARY SEARCH TREE =====")

    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Inorder Traversal:")
    bst.inorder()

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting 20 (leaf):")
    bst.inorder()

    bst.insert(65)
    bst.delete(60)
    print("After deleting 60 (one child):")
    bst.inorder()

    bst.delete(30)
    print("After deleting 30 (two children):")
    bst.inorder()

    print("\n===== GRAPH =====")

    g = Graph()

    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7),
        ('B','E',3), ('C','E',1), ('D','F',5),
        ('E','D',2), ('E','F',6), ('C','F',8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("\nAdjacency List:")
    g.print_graph()

    print("\nBFS from A:")
    g.bfs('A')

    print("\nDFS from A:")
    g.dfs('A')
    
    