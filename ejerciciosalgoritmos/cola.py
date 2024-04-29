class Queue:
    def __init__(self):
        self.elements = []
    def arrive (self,element):
        self.elements.append(element)
    def attention (self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else :
            return None
    def size(self):
        return len(self.elements)
    def on_front(self):
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            return None
    def move_to_end (self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
