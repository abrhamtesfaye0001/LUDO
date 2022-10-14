class FixedSizeQueue:
    def __init__(self,size=10):
        self.size = size
        self.container = []
    def push(self,new_item):
        if(len(self.container)<self.size):
            self.container.append(new_item)
            return new_item
        else:
            self.pop()
            self.container.append(new_item)
            return new_item
    def pop(self):
        if(len(self.container)==0):
            return None
        return self.container.pop(0)
    def peek_head(self):
        if(len(self.container)==0):
            return None
        return self.container[0]
    def peek_tail(self):
        if(len(self.container)==0):
            return None
        return self.container[-1]
    def __str__(self):
        rep = ""
        for i in range(len(self.container)-1,-1,-1):
            rep += str(self.container[i])+" => "
        return rep
    def toList(self):
        return self.container