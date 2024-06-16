import queue

class MyStack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.top = None
    
    def push(self, x: int) -> None:
        self.q1.put(x)
        self.top = x
        

    def pop(self) -> int:
        
        return self.top
    
    def top(self) -> int:
        return self.top

    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()