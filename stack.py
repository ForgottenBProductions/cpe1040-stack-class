class Stack():
    def __init__(self, sample): 
        self.stack = []
        self.sample = sample
        print("New Stack object")


    def pop(self): 
        print("Popping...")
        return self.stack.pop()

    def push(self, value): 
        if not isinstance(value, type(self.sample)): 
            raise ValueError('Expected integer but got {}'.format(type(value))) 
        else:
            self.stack.append(value) 
            print("Pushing...")



class IntStack(Stack): 
    def __init__(self):
        Stack.__init__(self,0)
