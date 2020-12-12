class Cell:
    def __init__(self, n):
        self.n = n

    def __int__(self):
        return self.n



    def __bool__(self):
        return bool(self.n)

a = Cell(3)
b = Cell(2)
c = Cell(0)

print(sum(map(bool,[a,b,c])))