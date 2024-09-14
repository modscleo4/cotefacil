from typing import Optional, Self


class BinarySearchTreeNode:
    left: Optional[Self]
    right: Optional[Self]
    value: int


    def __init__(self, value: int) -> None:
        self.left = None
        self.right = None
        self.value = value


    def insert(self, value: int) -> Self:
        '''
        Insert a value into the binary tree.
        '''
        if value <= self.value:
            if self.left is None:
                self.left = type(self)(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = type(self)(value)
            else:
                self.right.insert(value)

        return self


    def delete(self, value: int) -> Optional[Self]:
        '''
        Delete a value from the binary search tree.
        If the value is not present, return None.
        When deleting the root node, return the new root node.
        '''

        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_larger_node = self.right.min()
            self.value = min_larger_node
            self.right = self.right.delete(min_larger_node)

        return self


    def find(self, value: int) -> Optional[Self]:
        '''
        Find a node with a specific value in the binary tree.
        '''

        if value == self.value:
            return self
        elif value < self.value:
            return self.left.find(value) if self.left else None
        else:
            return self.right.find(value) if self.right else None


    def contains(self, value: int) -> bool:
        '''
        Check if a value is present in the binary tree.
        '''

        return bool(self.find(value))


    def height(self) -> int:
        '''
        Calculate the height of the tree (longest path from root to leaf).
        '''

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)


    def size(self) -> int:
        '''
        Calculate the size of the tree (number of nodes).
        '''

        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size


    def is_balanced(self) -> bool:
        '''
        Check if the tree is balanced.
        '''

        if self is None:
            return True

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = self.left.is_balanced() if self.left else True
        right_balanced = self.right.is_balanced() if self.right else True

        return left_balanced and right_balanced


    def min(self) -> int:
        '''
        Find the minimum value in the tree (leftmost node).
        '''

        if self.left is None:
            return self.value

        return self.left.min()


    def max(self) -> int:
        '''
        Find the maximum value in the tree (rightmost node).
        '''

        if self.right is None:
            return self.value

        return self.right.max()


    def traverse_inorder(self) -> list[int]:
        '''
        Traverse the binary tree in inorder (left, root, right) and return a list of values.
        '''

        result: list[int] = []
        if self.left:
            result.extend(self.left.traverse_inorder())

        result.append(self.value)

        if self.right:
            result.extend(self.right.traverse_inorder())

        return result


    def traverse_preorder(self) -> list[int]:
        '''
        Traverse the binary tree in preorder (root, left, right) and return a list of values.
        '''

        result: list[int] = [self.value]
        if self.left:
            result.extend(self.left.traverse_preorder())

        if self.right:
            result.extend(self.right.traverse_preorder())

        return result


    def traverse_postorder(self) -> list[int]:
        '''
        Traverse the binary tree in postorder (left, right, root) and return a list of values.
        '''

        result: list[int] = []
        if self.left:
            result.extend(self.left.traverse_postorder())

        if self.right:
            result.extend(self.right.traverse_postorder())

        result.append(self.value)
        return result


    def traverse_level(self) -> list[int]:
        '''
        Traverse the binary tree in level (root, left, right) and return a list of values.
        '''

        result: list[int] = []
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
