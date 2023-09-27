class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def prepend(self,data):
        newnode=Node(data)
        #check kif the list is empty
        if self.__head is None:
            self.__head=newnode
            self.__tail=newnode
        else:
            #when there is atleast one node
            newnode.next=self.__head
            self.__head.prev=newnode
            self.__head=newnode
            newnode.prev=None
        self.__size+=1
    def append(self,data):
        newnode=Node(data)
        #check kif the list is empty
        if self.__head is None:
            self.__head=newnode
            self.__tail=newnode
        else:
            self.__tail.next=newnode
            newnode.prev=self.__tail
            self.__tail=newnode #newnode is our tailnode
        self.__size+=1
    
    def traverse_fw(Self):
        currnode=Self.__head
        while currnode:    #while the current node is not null
            print(currnode.data)
            currnode=currnode.next

    def traverse_bw(self):
        currnode=self.__tail
        while currnode:
            print(currnode.data)
            currnode=currnode.prev
    def lsitSize(self):
        return self.__size
        

if __name__=="__main__":
    mylist=Doubly()

    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
     
    mylist.prepend(0)
    mylist.prepend(-1)
    mylist.prepend(-2)

    mylist.traverse_bw()
    print()
    mylist.traverse_fw()
    print()

    print(mylist.lsitSize())

    

    

