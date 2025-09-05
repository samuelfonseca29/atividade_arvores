# atividade_4.py

from graphviz import Digraph
import random

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # altura do nó, importante para AVL

class AVLTree:
    def __init__(self):
        self.root = None

    # Altura do nó
    def _height(self, node):
        if not node:
            return 0
        return node.height

    # Fator de balanceamento
    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Rotação simples à direita
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Rotacionar
        x.right = y
        y.left = T2

        # Atualizar alturas
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    # Rotação simples à esquerda
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Rotacionar
        y.left = x
        x.right = T2

        # Atualizar alturas
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    # Inserção
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        # Inserção normal BST
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # não permite duplicados

        # Atualizar altura
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Verificar fator de balanceamento
        balance = self._get_balance(node)

        # Rotação: LL
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        # Rotação: RR
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        # Rotação: LR
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Rotação: RL
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Visualização com Graphviz
    def visualize(self, filename="avl_tree"):
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
# Demonstração Árvores Fixas
# ---------------------------

print("=== AVL com Rotação Simples (LL ou RR) ===")
avl_simple = AVLTree()
for v in [10, 20, 30]:  # forçando rotação RR
    avl_simple.insert(v)
    avl_simple.visualize(f"avl_simple_{v}")

print("=== AVL com Rotação Dupla (LR ou RL) ===")
avl_double = AVLTree()
for v in [10, 30, 20]:  # forçando rotação RL
    avl_double.insert(v)
    avl_double.visualize(f"avl_double_{v}")

# ---------------------------
# Demonstração Árvores Aleatórias
# ---------------------------

print("\n=== AVL com Valores Aleatórios ===")
random_values = random.sample(range(1, 201), 20)
avl_random = AVLTree()
for v in random_values:
    avl_random.insert(v)

print("Valores aleatórios inseridos:", random_values)
avl_random.visualize("avl_random_tree")
