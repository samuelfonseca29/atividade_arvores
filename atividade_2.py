# atividade_2.py

from graphviz import Digraph
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserção
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        elif value > current.value:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)
        # valores duplicados não são inseridos

    # Busca
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if not current:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    # Remoção
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if not current:
            return current
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Caso 1: Nó sem filhos
            if not current.left and not current.right:
                return None
            # Caso 2: Nó com um filho
            elif not current.left:
                return current.right
            elif not current.right:
                return current.left
            # Caso 3: Nó com dois filhos
            temp = self._min_value_node(current.right)
            current.value = temp.value
            current.right = self._delete_recursive(current.right, temp.value)
        return current

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Altura
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return -1  # altura de árvore vazia é -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    # Profundidade
    def depth(self, value):
        return self._depth_recursive(self.root, value, 0)

    def _depth_recursive(self, node, value, depth):
        if not node:
            return -1  # valor não encontrado
        if value == node.value:
            return depth
        elif value < node.value:
            return self._depth_recursive(node.left, value, depth + 1)
        else:
            return self._depth_recursive(node.right, value, depth + 1)

    # Visualização com Graphviz
    def visualize(self, filename="tree"):
        dot = Digraph()
        def add_nodes_edges(node):
            if not node:
                return
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                add_nodes_edges(node.right)
        add_nodes_edges(self.root)
        dot.render(filename, view=True, format="png")

# ---------------------------
# Demonstração da Árvore Fixa
# ---------------------------

print("=== Árvore com Valores Fixos ===")
fixed_values = [55, 30, 80, 20, 45, 70, 90]
bst_fixed = BinarySearchTree()
for v in fixed_values:
    bst_fixed.insert(v)

bst_fixed.visualize("fixed_tree")
print("Busca 45:", bst_fixed.search(45))
bst_fixed.delete(30)
bst_fixed.insert(60)
print("Altura da árvore:", bst_fixed.height())
print("Profundidade do nó 45:", bst_fixed.depth(45))
bst_fixed.visualize("fixed_tree_after_ops")

# ---------------------------
# Demonstração da Árvore Aleatória
# ---------------------------

print("\n=== Árvore com Valores Aleatórios ===")
random_values = random.sample(range(1, 201), 15)
bst_random = BinarySearchTree()
for v in random_values:
    bst_random.insert(v)

print("Valores aleatórios inseridos:", random_values)
bst_random.visualize("random_tree")
print("Altura da árvore aleatória:", bst_random.height())
