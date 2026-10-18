class Vector:
    def __init__(self, l):
        self.l = l

    def __add__(self, other):
        result = [self.l[i] + other.l[i] for i in range(len(self.l))]
        return Vector(result)

    def __mul__(self, other):
        return sum(self.l[i] * other.l[i] for i in range(len(self.l)))

    def __str__(self):
        return f"{self.l[0]}i + {self.l[1]}j + {self.l[2]}k"

    def __len__(self):
        return len(self.l)


v = Vector([7, 8, 10])

print(v)
print(len(v))