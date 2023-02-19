class squares:
    def __init__(self,x):
        self.x=x
    def __iter__(self):
        return self
    def __next__(self):
        raise 