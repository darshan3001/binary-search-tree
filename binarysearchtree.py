class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key==data:
            return
        elif data < self.key:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)

    def search(self,data):
        if self.key == data:
            print('found!!!')
        elif data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print('not found!!!')
        else:
            if self.right:
                self.right.search(data)
            else:
                print('not found!!!')
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=' -- ')
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.key,end=' -- ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key,end=' -- ')

    def delete(self,data):

        if self.key is None:
            print('\nTree is empty')

        if data < self.key:
            if self.left:
                self.left=self.left.delete(data)
            else:
                print('\nThe value you entered is not present')

        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print('\nThe value you entered is not present')

        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.right
                self = None
                return temp
            node=self.right
            while node.left:
                node=node.left
            self.key=node.key
            self.right=self.right.delete(node.key)
        return self             

n=Node(9)
li=[5,4,1,8,44,55,11,25,12,45,0,21,9]
for i in li:
    n.insert(i)
n.search(0)
print('inorder:')
n.postorder()
n.delete(11)

