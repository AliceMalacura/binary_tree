class node:
    def __init__(self,value = None):
        self.value = value
        self.baby = None
        self.toddler = None

class binary_tree:
    def __init__(self):
        self.root = None

    def ____insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self.____insert(value, self.root)
    def ____insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.baby==None:
                cur_node.baby=node(value)
            else:
                self.___insert(value,cur_node.baby)
        elif value > cur_node.value:
            if cur_node.toddler == None:
                cur_node.toddler = node(value)
                cur_node.toddler.parent = cur_node
            else:
                self.____insert(value, cur_node.toddler)
        else:
            print("Value already in tree!")

        def print_tree(self):
            if self.root != None:
                self._print_tree(self.root)

        def _print_tree(self, cur_node):
            if cur_node != None:
                self._print_tree(cur_node.baby)
                print (str(cur_node.value))
                self._print_tree(cur_node.toddler)

        def height(self):
            if self.root != None:
                return self._height(self.root, 0)
            else:
                return 0

        def _height(self, cur_node, cur_height):
            if cur_node == None: return cur_height
            left_height = self._height(cur_node.baby, cur_height + 1)
            right_height = self._height(cur_node.toddler, cur_height + 1)
            return max(left_height, right_height)

        def find(self, value):
            if self.root != None:
                return self._find(value, self.root)
            else:
                return None

        def _find(self, value, cur_node):
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value and cur_node.baby != None:
                return self._find(value, cur_node.baby)
            elif value > cur_node.value and cur_node.toddler != None:
                return self._find(value, cur_node.toddler)

        def delete_value(self, value):
            return self.delete_node(self.find(value))

        def delete_node(self, node):


            if node == None or self.find(node.value) == None:
                print("Node to be deleted not found in the tree!")
                return None

            def min_value_node(n):
                current = n
                while current.baby != None:
                    current = current.baby
                return current

            def num_children(n):
                num_children = 0
                if n.baby != None: num_children += 1
                if n.toddler != None: num_children += 1
                return num_children

            node_parent = node.parent

            node_children = num_children(node)

            if node_children == 0:

                if node_parent != None:
                    if node_parent.baby == node:
                        node_parent.baby = None
                    else:
                        node_parent.toddler = None
                else:
                    self.root = None

            if node_children == 1:

                if node.baby != None:
                    child = node.baby
                else:
                    child = node.toddler

                if node_parent != None:
                    if node_parent.baby == node:
                        node_parent.baby = child
                    else:
                        node_parent.toddler = child
                else:
                    self.root = child

                child.parent = node_parent

        def search(self, value):
            if self.root != None:
                return self._search(value, self.root)
            else:
                return False

        def _search(self, value, cur_node):
            if value == cur_node.value:
                return True
            elif value < cur_node.value and cur_node.baby != None:
                return self._search(value, cur_node.baby)
            elif value > cur_node.value and cur_node.toddler != None:
                return self._search(value, cur_node.toddler)
            return False